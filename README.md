# Trading Automation

유튜브에 소개된 매매 전략을 구조화하고 검증한 뒤, 향후 Binance Futures 자동매매 연구로 연결하기 위한 공개 개발 프로젝트입니다. GitHub 저장소는 Public이며 기본 브랜치는 main입니다(2026-11-10 도구 확인). 현재는 문서·설계 준비 단계이며 분석 프로그램, 주문 기능과 성과 측정 결과는 없습니다.

## 주요 구성 요소

| 경로 | 목적 및 현재 상태 |
| --- | --- |
| `youtube-analyzer/` | 영상 목록·자막 수집, AI 전략 추출과 Markdown·JSON 출력 계획 |
| `trading-bot/` | 분석과 분리된 주문 실행 컴포넌트 계획, 미구현 |
| `strategies/` | 향후 전략 문서·구조화 결과 저장 위치 |
| `tests/` | SSH ACG 갱신 도구의 결정적 mock 테스트, 분석·주문 앱 테스트는 미구현 |
| `scripts/` | Windows 노트북 SSH 접속·기기별 ACG 갱신·로컬 설치 도구 |
| `infrastructure/` | 서버·키 접속·SSH 보안·개발 도구·Clone·환경 검증 완료, 앱 운영 미검증 |
| `docs/` | 로드맵과 설계 결정 기록 |

## 사용 기술 및 개발 환경

- 현재: Windows 노트북, Git, GitHub CLI, Codex CLI, Markdown. 노트북 설치·인증·Clone·CLI 실행은 사용자 확인, main 동기화는 도구로 확인했습니다.
- 계획: Python 기반 분석, YouTube 데이터·자막 처리, AI 전략 추출, Binance Futures 연계, 네이버 클라우드 배치. 구체적 라이브러리와 아키텍처는 미확정입니다.
- Python 프로젝트 런타임 버전·의존성·설치·실행·린트·테스트 명령은 아직 설정하지 않았습니다. 구현 시 실제 검증한 명령과 지원 버전을 기록합니다.

SSH 보조 도구는 Windows PowerShell 5.1·Python 3.11.9·Ruff 0.14.4에서 검증했습니다. 분석·주문 앱의 도구 선정과는 별개입니다. 설치·접속·전용 인증 절차는 [SSH 접속 안내](docs/SSH_ACCESS.md)를 따릅니다.

저장소 루트의 보조 도구 setup·test·lint·format 검사:

```powershell
python -m pip install --target .venv-tools -r requirements-dev.txt
python -m unittest discover -s tests -p "test_*.py" -v
.\.venv-tools\bin\ruff.exe check scripts tests
.\.venv-tools\bin\ruff.exe format --check scripts tests
```

dry-run 실행: `powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\connect-developer.ps1 -DryRun -Profile provisioning`. 실제 접속은 `-DryRun` 없이 실행합니다. `provisioning`은 이번에 검증한 기존 생성용 인증이며 전용 `ssh-acg` 인증으로 대체할 대상입니다. 기본값은 `ssh-acg`이고 다른 프로필로 자동 전환하지 않습니다.

## 현재 개발 단계와 향후 계획

GitHub 초기 구축과 Public 전환은 완료했고, 노트북 작업 환경 구성은 사용자 확인을 받았습니다. 공개 개발을 위한 문서·제외 규칙을 마련했으며 [AGENTS.md](AGENTS.md)의 보안·AI 활용·테스트 기록 규칙을 계속 적용합니다. 승인된 네이버 클라우드 서버·키 접속·SSH 보안·개발 도구·Clone·UTF-8/JSON/로그·자원 검증은 완료했습니다. ChatGPT 계정 Codex 로그인은 확인됐고 GitHub CLI 인증의 현재 상태는 미검증이며 유튜브 분석·자동매매·백테스트·모의매매·위험 관리 기능과 실제 앱 운영은 미구현/미검증입니다.

2026-11-10에는 서버 구축·개발 환경 검증을 완료했고, 11월 11일에는 노트북의 SSH ACG 갱신 도구를 구현했습니다. 현재 IP 규칙 추가와 새 SSH 인증은 기존 설치본으로 검증했으며, 최종 검토본은 mock 테스트 26개를 통과했습니다. 실제 네트워크 전환·이전 관리 규칙 삭제, 전용 인증과 운영 보완·생성용 키 회수 확인은 남아 있습니다. 분석 앱은 아직 미구현입니다. 상세 내용은 [프로젝트 상태](PROJECT_STATUS.md), [다음 단계](NEXT_STEPS.md), [로드맵](docs/ROADMAP.md)에 기록합니다.

## AI 활용 개발 방식

ChatGPT는 요구사항 정리·설계 검토·개발 계획 수립을 지원하고, Codex CLI는 저장소 파일 수정·명령 실행·검증을 지원합니다. 현재 AI 활용 결과물에는 문서 정비·공개 상태 확인과 승인된 클라우드 리소스 생성·API 검증이 포함되며, 프로그램 구현이나 매매 성능 검증을 의미하지 않습니다. 사용자 확인 사실, 도구 검증 결과와 AI 제안을 구분하고 최종 판단은 사용자가 검토합니다. 설계 이유와 미결정 사항은 [의사결정 기록](docs/DECISIONS.md), 작업 기준은 [AGENTS.md](AGENTS.md)를 따릅니다.

## 보안 및 면책

API 키·비밀번호·인증 토큰·SSH 개인키·계정 식별 정보는 커밋하지 않습니다. 실거래 자격증명은 저장소 밖에서 관리하고 주문 기능은 분석과 분리하며, 구현 시 실거래는 기본 비활성화합니다. 백테스트·모의매매·위험 한도·복구 검증과 명시적 설정이 필요합니다.

외부 영상·자막·코드는 출처와 라이선스·재배포 권한을 확인한 범위에서만 추가합니다. 현재 저장소에 해당 원본 자료는 없습니다. 이 프로젝트는 학습·연구 목적이며 투자 조언이나 수익 보장을 제공하지 않습니다. 자동매매에는 원금 손실 위험이 있습니다.
