# Trading Automation

유튜브 매매 전략을 분석하고 향후 Binance Futures 자동매매 코드로 연결하기 위한 프로젝트입니다. 현재는 문서와 폴더를 정리한 단계이며 실제 개발·실행 테스트는 아직 확인되지 않았습니다.

## 구성

- `docs/`: 시스템 구상, 로드맵과 의사결정
- `youtube-analyzer/`: 영상 목록·자막 수집 및 AI 전략 추출 개발 위치. 구현 시 `src/` 사용
- `trading-bot/`: 선물 자동매매 개발 위치. 구현 시 `src/` 사용
- `strategies/`: 향후 전략 Markdown·JSON 결과 저장 위치
- `infrastructure/`: 서버 구축 계획과 운영 확인 기록
- `tests/`: 향후 자동 테스트와 fixture 위치

## 현재 상태

[프로젝트 상태](PROJECT_STATUS.md), [다음 단계](NEXT_STEPS.md), [로드맵](docs/ROADMAP.md), [의사결정](docs/DECISIONS.md), [작업 규칙](AGENTS.md)을 참고합니다.

개인 Windows 데스크톱에서 Codex CLI, Git과 GitHub CLI를 사용합니다. Codex CLI 기반 Python 분석 프로그램을 개발할 계획이며, Python 버전과 의존성·실행·린트·테스트 명령은 아직 정해지지 않았습니다. 설정 후 검증한 명령만 문서화합니다.

네이버 클라우드 서버는 아직 생성되지 않았습니다. 실제 주문 프로그램, 백테스트, 모의매매와 위험 관리 기능은 미구현입니다. 빈 Private GitHub 저장소 생성과 원격 연결은 완료했으며 최초 커밋·Push는 승인 대기입니다.

## 보안과 실행 원칙

API 키, 토큰, 비밀번호, SSH 개인키, 계정 식별 정보와 비공개 설정을 커밋하지 않습니다. 실거래는 구현 시 기본 비활성화하고 백테스트·모의매매·위험 한도·복구 검증 후 명시적 설정을 요구합니다.

다른 컴퓨터에서 사용할 설치·실행 명령과 Clone 주소는 실제 설정과 검증 후 추가합니다.
