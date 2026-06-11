# Notes — 개인 지식 관리 시스템

파이썬 헬퍼 스크립트와 Claude를 조합한 개인 지식 관리 워크플로우.

---

## 디렉토리 구조

```
notes/
├── inbox/                      # 원본 메모 투입구 (원본 보존)
│   ├── archive/                # 처리 완료된 원본 보관
│   └── README.md
├── processed/                  # Claude가 가공한 중간 결과물
├── projects/<name>/
│   ├── meetings/YYYY-MM-DD.md  # 회의록
│   ├── todos.md                # 체크박스 할 일
│   └── specs/<slug>.md         # 기획/스펙 문서
├── ideas/<slug>.md             # 독립 아이디어 노트
├── scripts/
│   ├── process_inbox.py        # inbox 스캔 → JSON 출력
│   └── archive_file.py         # 원본 → archive/ 이동
├── dashboard.html              # 전체 현황 (자동 생성)
└── CLAUDE.md                   # 이 파일
```

---

## 전체 워크플로우

### 1단계 — 메모 투입
사용자가 `inbox/` 에 파일을 직접 저장한다.
- 형식: `.md` 또는 `.txt`
- 파일명 권장: `YYYY-MM-DD_주제.md`
- 내용 형식 자유 (회의 메모, 아이디어, 할 일 목록 등 무관)

### 2단계 — 가공 (`/정리`)
Claude가 수행하는 작업:
1. `python scripts/process_inbox.py` 실행 → inbox 파일 목록 JSON
2. 각 파일을 읽어 **요약 + 키워드** 도출 (분류는 하지 않음)
3. `processed/YYYY-MM-DD_<원본파일명>.md` 에 저장 (`상태: 대기중`)
4. 처리 목록 출력 후 종료 — `/분류 를 실행하세요` 안내

### 3단계 — 분류 (`/분류`)
Claude가 수행하는 작업:
1. `processed/` 에서 `상태: 대기중` 파일 수집
2. 분류 제안 테이블 출력 (meeting / todo / idea / spec / skip)
3. **사용자 확인/수정 대기** → "저장해줘" 받으면 진행
4. 각 분류에 맞는 파일 생성/추가 (아래 참조)
5. 원본 `inbox/archive/` 이동, processed 파일 상태 `완료` 업데이트

| 분류 | 저장 위치 |
|------|-----------|
| `meeting` | `projects/<name>/meetings/YYYY-MM-DD.md` |
| `todo` | `projects/<name>/todos.md` |
| `idea` | `ideas/<slug>.md` |
| `spec` | `projects/<name>/specs/<slug>.md` |
| `skip` | 이동 없음 |

### 4단계 — 대시보드 (`/대시보드`, 필요할 때만)
사용자가 원할 때 실행. Claude가 파일 시스템을 읽어 `dashboard.html` 재생성 후 브라우저로 열기.

---

## 슬래시 명령

| 명령 | 설명 |
|------|------|
| `/정리` | inbox 스캔 → 요약 가공 → processed/ 저장 |
| `/분류` | processed/ 대기 파일 → 분류 확인 → 최종 저장 |
| `/대시보드` | dashboard.html 재생성 + 브라우저로 열기 |

---

## 회의록 템플릿

```markdown
# [프로젝트명] YYYY-MM-DD 회의

## 참석자

## 논의 내용

## 결정 사항

## 액션 아이템
| 담당 | 내용 | 마감 |
|------|------|------|
```

---

## 개발 환경

- 주 언어: **Python**
- 헬퍼 실행: `python scripts/process_inbox.py`
- Python 버전: 시스템 기본 (`python` 명령)

---

## 언어 규칙

- Claude는 **항상 한국어**로 응답한다 (사용자가 영어로 쓸 때는 영어로)
- 파일 내용은 한국어 마크다운으로 작성
