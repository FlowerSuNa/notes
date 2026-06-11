# 📋 Personal Notes — AI 기반 개인 지식 관리 시스템

Claude Code와 Python 헬퍼 스크립트를 조합한 개인 메모 정리·분류 워크플로우입니다.
회의 메모, 아이디어, 할 일을 `inbox/` 에 자유롭게 투입하면 Claude가 구조화된 문서로 가공하고 프로젝트별로 분류합니다.

---

## 주요 특징

- **원본 보존**: `inbox/` 에 저장한 파일은 `archive/` 로 이동될 뿐 삭제되지 않음
- **2단계 분류**: 정리(요약·가공) → 분류(사용자 확인 후 저장) 단계 분리로 실수 방지
- **슬래시 명령**: Claude Code 내에서 `/정리` `/분류` `/대시보드` 로 워크플로우 실행
- **Python 헬퍼**: inbox 스캔 및 파일 아카이브를 스크립트로 처리

---

## 디렉토리 구조

```
notes/
├── inbox/                        # 원본 메모 투입구 (파일 보존)
│   ├── archive/                  # 처리 완료된 원본 보관
│   └── README.md
├── processed/                    # Claude가 가공한 중간 결과물
├── projects/<name>/
│   ├── meetings/YYYY-MM-DD.md   # 회의록
│   ├── todos.md                  # 체크박스 할 일
│   └── specs/<slug>.md           # 기획·스펙 문서
├── ideas/                        # 독립 아이디어 노트
├── scripts/
│   ├── process_inbox.py          # inbox 스캔 → JSON 출력
│   └── archive_file.py           # 원본 → archive/ 이동
├── CLAUDE.md                     # 전체 워크플로우 문서 (Claude 지시서)
├── dashboard.html                # 전체 현황 대시보드 (자동 생성)
└── .claude/commands/             # 슬래시 명령 정의
    ├── 정리.md
    ├── 분류.md
    └── 대시보드.md
```

---

## 워크플로우

```
① inbox/ 에 메모 파일 저장  (.md 또는 .txt, 파일명 권장: YYYY-MM-DD_주제.md)
         ↓
② /정리  →  Claude가 요약·재구조화 → processed/ 저장
         ↓
③ /분류  →  분류 제안 확인/수정 → 확정 후 projects/ · ideas/ 에 저장
         ↓
④ /대시보드  (필요할 때만)  →  dashboard.html 재생성 + 브라우저 열기
```

---

## 요구사항

| 항목 | 버전 |
|------|------|
| [Claude Code](https://claude.ai/code) | 최신 |
| Python | 3.10 이상 |

별도 패키지 설치 없이 Python 표준 라이브러리만 사용합니다.

---

## 빠른 시작

```bash
# 1. 메모 작성
echo "오늘 회의 내용..." > inbox/2026-06-11_회의.md

# 2. Claude Code 실행
claude

# 3. 슬래시 명령 실행
/정리
/분류
```

---

## 슬래시 명령 요약

| 명령 | 설명 |
|------|------|
| `/정리` | inbox 스캔 → 요약·가공 → processed/ 저장 |
| `/분류` | processed/ 대기 파일 → 분류 확인 → 최종 저장 + 아카이브 |
| `/대시보드` | dashboard.html 재생성 + 브라우저 열기 |

---

> 전체 워크플로우 및 파일 형식 규칙은 [`CLAUDE.md`](CLAUDE.md) 를 참고하세요.
