# 저장소 작업 지침

## 프로젝트 구조 및 모듈 구성

이 저장소에는 현재 application code, tests, dependency manifests 또는 build configuration이 없습니다. 루트는 프로젝트 문서와 설정을 중심으로 유지합니다. 구현을 시작하면 application code는 `youtube-analyzer/`와 `trading-bot/` 아래 각 컴포넌트의 `src/`에, automated tests는 `tests/`에 배치합니다. 재사용 가능한 개발 유틸리티는 필요할 때 `scripts/`에 배치합니다. asset 디렉터리는 필요한 경우에만 추가하고 목적을 `README.md`에 기록합니다.

## Build, Test 및 개발 명령어

현재 build, test 또는 로컬 실행 명령어는 설정되어 있지 않습니다. 프로젝트 toolchain을 선택할 때 재현 가능한 setup, run, lint 및 test 명령어를 `README.md`와 해당 dependency manifest에 추가합니다. 필요한 runtime 버전을 명시합니다. 설정이 실제로 존재하고 검증되기 전에는 예시 명령어를 작동하는 명령어로 문서화하지 않습니다.

## Coding Style 및 Naming Conventions

선택한 구현 언어의 formatter와 관용적 작성 방식을 따릅니다. 각 파일 내 들여쓰기를 일관되게 유지하고, 설명적인 module 이름과 의도를 드러내는 이름을 사용합니다. 첫 source 파일을 추가할 때 formatter와 linter 설정도 함께 도입합니다. module은 하나의 목적에 집중하도록 유지하며, configuration, 외부 service 접근과 business logic을 하나의 module에 혼합하지 않습니다.

## Testing 지침

현재 testing framework나 coverage 기준은 정해져 있지 않습니다. 의미 있는 동작 변경마다 automated tests를 추가하고, 지원되는 경우 `test_<behavior>`처럼 동작을 설명하는 이름을 사용합니다. tests는 결정적이어야 하며 live accounts나 network services에 의존하지 않아야 합니다. framework를 도입할 때 test 명령어를 문서화합니다.

## Commit 및 Pull Request 지침

기존 이력의 `docs:` 등 목적 접두사와 간결한 명령형 commit 제목을 참고합니다. 변경은 하나의 목적에 집중합니다. Pull Request에는 목적, 동작 변경 요약, 관련 issue 링크와 수행한 검증을 기록합니다. 실행하지 못한 검사는 그 이유를 설명합니다.

## 보안 및 Configuration

credentials, account identifiers 또는 private configuration은 절대 commit하지 않습니다. placeholder configuration 예시를 제공하고 로컬 secret 파일을 ignore합니다. trading integration을 추가하면 tests에 mocks 또는 sandbox environments를 사용하고 live execution을 활성화하기 전에 명시적인 configuration을 요구합니다.

## 프로젝트 기록 및 작업 연속성

- 작업 시작 전에 `PROJECT_STATUS.md`와 `NEXT_STEPS.md`를 읽습니다.
- 구현됨, 테스트됨, 계획됨, 미검증 상태를 구분합니다. 근거 없이 서버 구축이나 live trading이 완료되었다고 주장하지 않습니다.
- 작업 종료 시 관련 문서, test 결과, 오류와 `NEXT_STEPS.md`를 갱신하고, 중요한 변경은 `CHANGELOG.md`에 기록합니다.
- 저장소 상대 경로를 사용하고, 다른 컴퓨터에서 작업할 수 있도록 runtime 버전과 재현 가능한 명령어를 기록합니다.
- 기존 파일과 Git history를 보존합니다. 명시적인 사용자 승인 없이 history 삭제, force-push 또는 기존 remote 내용 덮어쓰기를 하지 않습니다.
- GitHub remote repository 생성 및 최초 push 전에 최종 사용자 확인을 받습니다.

## Trading 및 Secret 처리

- Private repository라도 Binance keys, tokens, passwords, account identifiers, SSH private keys, private configuration, 용량이 큰 원본 영상, 불필요한 logs와 임시 파일은 절대 commit하지 않습니다.
- commit 전에 staged changes에서 secrets를 검사합니다. `.gitignore`는 실제 검사를 대신하지 않습니다.
- live execution은 구현 시 기본 비활성화합니다. 실사용 전에 명시적인 configuration을 요구하고 backtesting, paper trading, risk limits와 recovery를 검증합니다.
- 실제 provisioning과 operation의 근거가 확인될 때까지 Naver Cloud 서버 설정은 진행 중 / 검증 필요 상태로 취급합니다.

## 한글 텍스트 Encoding 및 검증

- 한글 텍스트와 Markdown은 명시적으로 UTF-8로 저장하며 기존 지침을 보존합니다.
- PowerShell console output encoding과 파일 저장 encoding은 별개로 취급합니다.
- 저장 후 실제 bytes를 strict UTF-8 decoding으로 다시 읽고, 예상한 한글, replacement characters 및 예상치 못한 물음표 연속 문자열을 검사합니다.
- console rendering을 신뢰할 수 없으면 ASCII-escaped JSON 또는 Unicode code points를 사용합니다.
- 실제 물음표로 치환된 텍스트는 encoding 변경으로 복구할 수 없습니다. 확인된 문맥만으로 재작성하고 재작성 사실을 기록합니다.
- 임시 검증 파일과 불필요한 backup은 Git에서 제외하고 commit 전에 staged content를 다시 검사합니다.

## 문서 작성 언어

- 앞으로 Codex가 생성하는 프로젝트 설명 및 진행 상황 문서는 기본적으로 한국어로 작성합니다.
- 명령어, 파일명, 경로 및 기술 용어는 영어 원문을 유지합니다.

## 공개 개발 및 AI 활용 규칙

- 모든 프로젝트 문서는 기본적으로 한국어로 작성하고 한글은 UTF-8로 저장한 뒤 위 Encoding 규칙에 따라 실제 bytes를 재검증합니다.
- 코드 수정 후 관련 테스트를 실행합니다. 실행하지 못한 항목은 이유와 함께 미검증으로 기록합니다.
- 작업 종료 시 `PROJECT_STATUS.md`와 `NEXT_STEPS.md`를 최신화하고 주요 변경은 `CHANGELOG.md`에 기록합니다.
- 설계 결정과 이유, 대안 및 미결정 사항은 `docs/DECISIONS.md`에 기록합니다.
- ChatGPT의 요구사항·설계 검토 역할과 Codex CLI의 파일 수정·명령 실행·검증 역할, 실제 AI 활용 범위와 한계를 문서에 기록합니다.
- 사용자가 직접 검증한 사실, 도구로 확인한 결과와 AI가 제안한 계획·추정을 구분합니다. AI 제안을 구현·검증된 성과로 기록하지 않습니다.
- Commit 전 스테이징된 파일의 실제 내용에서 민감정보를 검사하고 Push 전 Git diff와 변경 파일 목록을 확인합니다.
- 외부 영상·자막·코드의 출처, 라이선스 및 재배포 권한을 확인합니다. 권한이 확인되지 않은 원문·원본은 공개 저장소에 추가하지 않습니다.
- API 키, 비밀번호, SSH 개인키 및 인증 토큰은 커밋하지 않습니다. 실거래 자격증명은 저장소 밖에서 별도 관리하고 주문 기능은 분석 컴포넌트와 분리합니다.
- 공개 준비 작업의 Commit·Push는 사용자가 변경 사항과 검사 결과를 확인한 후 승인해야 합니다. Visibility 변경은 별도 명시적 요청이 있을 때만 진행합니다.
