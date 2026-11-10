# 프로젝트 상태

기준일: 2026-11-10. 사용자 확인, 도구 검증과 계획을 구분합니다.

| 항목 | 상태 | 근거 및 남은 작업 |
| --- | --- | --- |
| 기본 문서 및 폴더 | 생성 완료 | Markdown 12개와 .gitignore, 애플리케이션 코드·의존성 명세·빌드 설정·자동 테스트 없음 |
| GitHub 초기 구축 | 완료·검증됨 | Private, 기본 브랜치 main, 기존 커밋 5개 보존 |
| 노트북 작업 환경 | 사용자 확인 완료 | Windows 노트북에서 Git·GitHub CLI·Codex CLI 설치·인증·Clone·실행 완료 |
| main 동기화 | 직접 검증됨 | 이번 작업 시작 시 fetch 후 로컬 main·origin/main·원격 main이 6242684로 일치, 작업 폴더 깨끗함 |
| 공개 개발 준비 | 보완 중 | 문서·제외 규칙 보완, Commit·Push 승인 대기, Visibility 변경 없음 |
| Python 개발 환경 | 미설정 | 프로젝트 지원 런타임·의존성·포매터·린터·테스트 도구 선정 및 명령 검증 필요 |
| 유튜브 분석 시스템 | 계획·미구현 | 아키텍처, 영상 목록·자막 수집, AI 전략 추출, Markdown·JSON 스키마 설계 필요 |
| 네이버 클라우드 서버 | 미검증 | 기존 기록은 미생성. 실제 생성·접속·운영 증거 없음 |
| Binance Futures 주문 프로그램 | 미구현 | 분석과 분리된 주문 기능 설계 예정 |
| 백테스트·모의매매·위험 관리 | 미구현 | 실거래 전 위험 한도·복구까지 검증 필요 |
| 24시간 운영·매매 성능 | 미검증 | 실행·운영·성과 측정 근거 없음 |

## 환경과 확인 범위

- 개인 Windows 데스크톱에서 시작한 프로젝트를 현재 Windows 노트북에서 이어서 작업합니다. 노트북 설치·로그인·Clone·Codex CLI 실행 완료는 사용자 확인 사항입니다.
- 이번 환경에서 Git 2.56.0.windows.4, GitHub CLI 2.103.3, Python 3.11.9 실행을 확인했습니다. Python 설치 확인은 프로젝트 개발 환경 구성 완료를 의미하지 않습니다.
- GitHub 도구로 저장소 Private와 기본 브랜치 main을 직접 확인했습니다. 원격 생성·최초 Push는 이미 완료한 이력입니다.
- 클라우드 크레딧은 과거 사용자 제공 정보이며 현재 잔여액·기간·조건은 미확인입니다. 상품 제공 여부·사양·비용을 구축 전에 확인합니다.
- 과거 데스크톱의 CLI 오류를 현재 노트북 문제로 단정하지 않습니다.

## 이전 검증 및 보존 기록

- 과거 한글이 실제 물음표로 손상된 문서 11개를 확인된 문맥에 따라 재작성했습니다. 원문 복원이 아니며 관련 이력은 보존합니다.
- 사용자 제공 이전 보안 감사 결과: 전체 커밋 5개와 작업 파일 Gitleaks 탐지 0건, 인증정보·개인정보 유출 미발견, Issues·PR·Actions·Releases 등 확인 완료. 연결된 GitHub Projects 없음은 사용자 직접 확인 사항입니다.
- 이번 작업에서도 전체 이력과 변경 파일을 다시 검사합니다. 탐지 0건은 사용한 검사 범위의 결과이며 모든 위험 부재의 증명은 아닙니다.

## 이번 공개 준비 작업

- .gitignore에 로컬 인증 설정, DB·저널·백업, analysis/raw/ 규칙을 추가하고 SQL 소스·공개 예시·fixture 처리 기준을 명시했습니다.
- 공개 개발 규칙, AI 활용 범위, 외부 자료 권리 확인, 설계 결정 이유, staged content 검사와 Push 전 diff 확인 절차를 문서화했습니다.
- 서버·분석·주문 프로그램은 완료로 변경하지 않았습니다. 애플리케이션 테스트는 코드와 framework가 없어 실행 대상이 없습니다.
- 검사 결과와 승인 대기 상태는 아래 검증 기록과 NEXT_STEPS.md에 기록합니다. 새 Commit·Push·변경 이력 검사는 승인 후 진행합니다.

## 공개 준비 검증 기록 (Commit 전)

- Markdown 12개: 실제 bytes의 엄격한 UTF-8 디코딩, 한글 존재, 대체 문자·연속 물음표·대표적인 깨짐 패턴 및 상대 링크 검사 통과.
- .gitignore: 제외 25개·허용 15개 사례 통과. 중첩 analysis/raw/ 누락을 수정 후 재검증했습니다. SQL 소스, JSON·SQL fixture, 지정 경로 DB fixture·예시를 허용합니다.
- Gitleaks 8.30.1: 전체 이력 5개 및 작업 파일 탐지 0건. 공식 릴리스 SHA256 체크섬을 대조했고 도구는 저장소 밖 임시 폴더에 있습니다.
- 재현 명령: 임시 도구 디렉터리를 PATH에 추가한 환경에서 `gitleaks git . --log-opts="--all --full-history" --redact --no-banner`, `gitleaks dir . --redact --no-banner`. 새 커밋 후에도 전체 이력 검사를 반복합니다.
- Git diff와 변경 파일 검토, `git diff --check` 통과. LF→CRLF 안내는 Git의 줄바꿈 정규화 경고이며 UTF-8 손상과 구분합니다.
- GitHub API 직접 확인: Private, 기본 브랜치 main. Visibility 변경 요청·실행 없음.
- 오류: 최초 fetch의 sandbox 쓰기·네트워크 제한은 승인된 재실행으로 해결. Gitleaks PATH 부재는 임시 도구 준비로 해결.
- staged content 검증: Git index의 전체 13개 파일을 임시 경로로 추출해 Gitleaks 검사 탐지 0건, staged diff 검사도 탐지 0건. index의 Markdown 12개 UTF-8·한글·손상 패턴·상대 링크 검사 통과. 개인키·토큰·인증정보 대입·이메일·IPv4 보조 패턴 검사도 탐지 0건입니다.
- staged diff 재현 명령: `gitleaks git . --pre-commit --staged --redact --no-banner`. 전체 staged 파일 검사는 `git show :경로`의 바이트를 추출해 `gitleaks dir`로 수행했습니다.
- 프로그램·서버 검증은 이번 문서 검사 범위에 포함되지 않습니다. 현재 Commit·Push 승인 대기이며, 새 커밋 생성 후 전체 이력을 다시 검사합니다.
