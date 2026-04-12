## 프로젝트 개요

# ==== 예시 ====
Go 기반 실시간 투표 마이크로서비스
SSE를 사용해 결과를 스트리밍한다.
아키텍처 개요는 docs/architecture.md 문서를 참고한다.
# ==============


## 개발 환경

# ==== 예시 ====
go mod download
cp .env .example .env
# ==============


## 실행
세부 실행 방법은 backend/, frontend/ 각각의 AGENTS.md를 따른다

# ==== 예시 ====
go run cmd/pulse/main.go
# 기본 접속 주소: http://localhost:8080
# ==============


## 구조 요약

# ==== 예시 ====
domain/ # 비즈니스 로직(외부 의존성 없음)
app/ # 유즈케이스(domain만 의존)
adapters/ # HTTP, DB, Redis 어댑터 구현
의존성 방향: adapters -> app -> domain
# ==============


## 테스트 정책

- 모든 변경은 검증을 통과해야 한다
- 테스트를 끄지 않는다
- 임시 회피 코드 금지
- 최소 변경 원칙 유지
- 실행: ./scripts/verify.sh

상세 내용은 docs/testing-guide.md 참고


## 반드시 지켜야 할 사항

# ==== 예시 ====
1. 하드코딩 값 사용을 지양한다
2. 커밋 전 검증 스크립트를 통과해야 한다
# ==============




