---
name: dev-cycle
description: End-to-end development cycle with test, fix, and review loop
---

# Dev Cycle Skill

This skill executes a full development workflow using multiple agents.

## Flow

1. coder → implement feature
2. tester → generate tests
3. run verify script
4. if failed → fixer → retry
5. if success → reviewer

---

## Execution Steps

### 1. Implement

Use agent: coder

- Read PRD.md, plan.md, WBS.md
- Implement required feature

---

### 2. Generate Tests

Use agent: tester

- Create missing tests
- Focus on edge cases

---

### 3. Verify

Run:

```bash
bash scripts/verify.sh
