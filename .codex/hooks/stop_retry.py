#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path


STATE_PATH = Path("./state/retry_state.json")
MAX_RETRIES = 3


def load_state():
    if not STATE_PATH.exists():
        return {"count": 0}
    try:
        return json.loads(STATE_PATH.read_text())
    except Exception:
        return {"count": 0}


def save_state(state):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2))


def reset_state():
    save_state({"count": 0})


def run_verify():
    proc = subprocess.run(
        ["bash", "../scripts/verify.sh"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    return proc.returncode, proc.stdout


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    # 🔥 중요: 이미 retry 루프 중이면 무한 루프 방지
    if payload.get("stop_hook_active"):
        sys.exit(0)

    state = load_state()
    count = state.get("count", 0)

    code, output = run_verify()

    # ✅ 성공
    if code == 0:
        reset_state()
        sys.exit(0)

    # ❌ 최대 재시도 초과
    if count >= MAX_RETRIES:
        print(json.dumps({
            "decision": "block",
            "reason": (
                "Verification failed after maximum retries.\n\n"
                f"Retry count: {count}/{MAX_RETRIES}\n\n"
                "Fix manually."
            )
        }))
        sys.exit(0)

    # 🔁 retry 증가
    state["count"] = count + 1
    save_state(state)

    short_output = output[-4000:]

    print(json.dumps({
        "decision": "block",
        "reason": (
            "Verification failed.\n\n"
            f"Retry count: {state['count']}/{MAX_RETRIES}\n\n"
            "Fix the root cause and run again.\n\n"
            "Recent output:\n"
            f"{short_output}"
        )
    }))


if __name__ == "__main__":
    main()
