# 네이버 클라우드 영상 분석 서버 조사

## 노트북 추가 인계 (2026-11-10)

근거: 전달 ZIP의 `HANDOFF.txt`와 추가 전용 패치를 이번 서버 세션에서 직접 읽었습니다. 아래 접속 복구 검증은 노트북 측 도구 결과의 전달 기록이며 이번 서버 세션에서 클라우드 변경이나 접속 시험을 재실행한 결과가 아닙니다. 노트북 원본 작업 폴더는 직접 확인하지 않았습니다.

### 후속 developer 타임아웃 복구

연구용 프로필로 서버 RUN·Public IP 실제 연결·대상 일치와 NIC의 실제 ACG를 조회했습니다. ipify에서 새로 확인한 현재 노트북 공인 IPv4가 기존 TCP 22 /32와 달랐습니다. 사용자 교체 승인에 따라 유효한 provisioning 권한으로 이전 규칙을 제거하고 ACG 비동기 설정 반영 중에는 추가 호출하지 않았습니다. 이후 RUN·inbound 0개를 재조회하고 현재 노트북 /32를 추가해 최종 inbound 1개·이전 규칙 없음·outbound 5개 유지를 검증했습니다. 로컬 private 입력도 새 /32로 갱신했습니다.

Windows Test-NetConnection의 실제 대상 일치·TCP 22 true를 확인한 뒤 기존 ED25519 known_hosts·StrictHostKeyChecking=yes·노트북 키를 그대로 사용해 developer 새 세션·sudo -n true를 검증했습니다. 호스트 키 오류 없이 SSH 종료 코드 0입니다. 전체 인터넷 개방·계정 권한 확대·SSH 설정 변경/재설치·서버 재생성·Commit·Push는 하지 않았습니다. 실제 IP와 식별자는 저장소 밖에서만 관리합니다. 생성용 인증은 이번에 유효했으며 키 비활성화·정책 회수는 여전히 사용자 콘솔 확인 대상입니다.

## 오늘 최종 구축 상태와 운영 경계 (2026-11-10)

오늘은 서버 구축·개발 환경 준비까지 완료하고 종료합니다. 아래 단계별 과거 기록의 미접속·미로그인·미생성 문구보다 이 절과 현장 점검 결과가 우선합니다. 최초 정리 이후 전달 ZIP의 HANDOFF·manifest·추가 패치를 직접 검토해 통합했습니다. 노트북 원본 작업 폴더는 직접 확인하지 않았습니다.

| 항목 | 최종 상태와 근거 |
| --- | --- |
| 구성 | 기존 생성·조회 검증: trading-vpc, trading-public, KR-1, youtube-analyzer 1대, c2-g3, 2 vCPU·4GB, Ubuntu 24.04, CB1 30GB, Public IP 1개. 시간제 MTRAT 요청, 실제 청구 화면은 미확인 |
| 제외 자원 | NAT Gateway·Micro-g3는 생성하지 않음 |
| SSH | 현재 접속 IP /32의 TCP 22만 허용. 학교망 실패 뒤 핫스팟 /32로 교체해 TCP 연결 성공. 학교망 자체 차단 여부는 미확정 |
| 호스트 키 | 최초 이미지 문자 추출 오류를 정정한 후 신뢰 콘솔 지문과 재대조 성공(사용자 전달 사실 및 기존 최종 일치 기록). 실제 IP·지문·키는 공개하지 않음 |
| 계정·보안 | developer 키·sudo·일반 사용자 새 세션 검증 후 비밀번호·root 원격 로그인 차단. 콘솔 root 복구 경로 유지 |
| 실제 SSH 재접속 | 이번 사용자 확인: SSH를 실제 종료한 뒤 developer 재접속·sudo 성공. 기존 도구 tmux PTY 시험과 구분. 재부팅 후 접속은 미검증 |
| 개발 환경 | Python 3.12.3·venv, Git 2.43.0, Node.js 26.13.0·npm 11.20.0, Codex 0.167.0·tmux 3.4 설치·실행, Clone·UTF-8·한글 JSON·로그·메모리·디스크 검증. 상세 수치는 아래 기록 |
| 인증·AI | 기존 도구로 ChatGPT 계정 Codex 로그인 확인. 유료 AI API 호출 없음. 구독 로그인 기반 분석은 향후 검증 계획이며 프로그램은 미개발 |
| 비용 | 기존 공식 단가·30일 추정: 상시 VAT 포함 약 81,101원, 하루 4시간 약 20,381원. 디스크·Public IP 보유는 중지 중에도 과금. 아래 가정·출처·미확인 조건 유지 |

### 재현 및 복구 절차의 검증 수준

다음 명령은 기존 현장 검증에서 사용한 조회·점검입니다. 오늘 서버 설정을 다시 변경한 것은 아닙니다.

```bash
sudo -n true
python3 --version
git --version
node --version
npm --version
codex --version
tmux -V
sudo /usr/sbin/sshd -t
```

SSH 재접속 예시(placeholder)는 아래와 같습니다. 실제 기기별 키·주소와 신뢰 콘솔에서 대조한 known_hosts가 필요합니다. 이 예시 문자열 자체는 실행하지 않았습니다.

```bash
ssh -o StrictHostKeyChecking=yes -i <PRIVATE_KEY_PATH> developer@<SERVER_PUBLIC_IP>
```

- SSH 설정 복구 계획·미검증: 콘솔 root 접속 또는 유지 중인 sudo 세션에서 기존 root 전용 설정 백업의 존재·내용을 확인하고 필요한 설정만 복원한 뒤 문법·유효 설정과 새 developer 세션을 검사합니다. 실제 복원·복구 시험은 수행하지 않았습니다. 기존 설정 백업은 전체 서버 백업과 다릅니다.
- 백업 계획·미검증: 저장소 밖 암호화 목적지·보관 기간을 정하고 필요한 데이터·설정을 선별해 백업한 뒤 별도 복구 환경에서 무결성과 접속을 검사합니다. 데이터 백업·스냅샷 생성·복구는 미실행입니다.
- 중지 계획·미검증: 작업 저장·세션 확인 후 사용자 승인으로 NAVER Cloud 콘솔에서 대상 서버를 중지하고 STOP 상태와 청구 조건을 확인합니다. OS shutdown만으로 과금 정지를 보장하지 않습니다. 자동 정지·중지 명령은 구현·실행하지 않았습니다.
- 재시작 계획·미검증: 승인 후 콘솔에서 시작하고 상태·현재 접속 /32·신뢰 호스트 키·developer 접속·sudo를 확인합니다. 재부팅 후 재접속 시험은 미실행입니다.
- 반납 계획·미검증: 복구 가능한 백업 확인과 사용자 승인 후 서버·연결 디스크·Public IP·네트워크 의존성을 개별 확인해 반납하고 잔여 과금 자원을 조회합니다. 중지를 반납으로 간주하지 않으며 삭제·반납 명령은 제시하거나 실행하지 않았습니다.
- 남은 작업: 4시간 자동 정지, Remote-SSH 실제 연결, 데스크톱 별도 키, 재부팅·장기 운영, 백업·복구, 비용 알림, 생성용 API 키 비활성화·정책 해제 완료 확인. 현재 클라우드·청구 상태는 이번에 재조회하지 않았습니다.

## 서버 현장 마무리 점검 (2026-11-10)

이 절은 이번 developer 서버 세션에서 직접 확인한 최신 결과입니다. 아래 이전 기록의 미로그인·인계 대기 상태보다 우선합니다. 노트북의 미커밋 문서나 로컬 파일은 이 서버에서 확인하지 않았습니다.

- 완료·도구 검증: 현재 사용자 developer(UID 1001), `sudo -n true` 종료 코드 0. sudo로 시스템 설정은 변경하지 않았습니다.
- 완료·도구 검증: `codex login status` 종료 코드 0, 로그인 방식 ChatGPT. 명령 출력을 메모리에서 판별해 방식만 기록했으며 인증 파일·토큰·키 값은 출력하지 않았습니다. 인증 갱신·유료 API 호출 성공을 검증한 것은 아닙니다. 확인 방식은 [OpenAI 공식 인증 문서](https://learn.chatgpt.com/docs/auth)를 참고했습니다.
- 완료·도구 검증: Python 3.12.3, Git 2.43.0, Node.js v26.13.0, npm 11.20.0, codex-cli 0.167.0, tmux 3.4. venv는 Python 표준 모듈이며 별도 버전 대신 임시 환경 생성·Python 3.12.3 실행·sys.prefix 분리 확인을 통과했습니다. 임시 환경은 정리했습니다.
- 완료·도구 검증: 격리된 tmux 소켓·임시 세션에서 detached 생성, PTY 접속, 분리, 동일 pane 재접속과 재분리를 검증했습니다. 각 접속 시 attached=1, 분리 후 attached=0, 클라이언트 종료 코드 0을 확인했습니다. 테스트 세션만 정리했고 기존 tmux 서버는 조작하지 않았습니다. 실제 SSH 연결 단절·재접속 시험은 이번 점검에 포함되지 않습니다.
- 완료·도구 검증: main HEAD·origin/main·`git ls-remote --exit-code origin refs/heads/main`의 원격 main 모두 8d2ddf1e967c4a1d8cf11a0cb255862ba78193c1. `git rev-list --left-right --count HEAD...origin/main`은 0/0, staged 변경은 없습니다. fetch·Commit·Push는 하지 않았습니다.
- 보존: 시작 시 미커밋 문서 CHANGELOG.md, NEXT_STEPS.md, PROJECT_STATUS.md, README.md, docs/DECISIONS.md, infrastructure/NAVER_CLOUD.md와 미추적 infrastructure/infra-provisioner-policy.json을 확인했습니다. 점검 중 해시가 유지됐음을 확인한 뒤 기존 내용을 보존하며 이번 기록을 추가했습니다. 노트북 작업 사본과 동일하다고 주장하지 않습니다.
- 미검증·남은 작업: 생성용 Access Key 비활성화·정책 해지 완료는 사용자 콘솔 확인 필요. GitHub CLI 로그인은 이번 점검 대상이 아니므로 현재 상태 미검증. 현재 청구·크레딧·클라우드 리소스·SSH 보안 설정은 이번에 재조회하지 않았습니다. 하루 4시간 자동 정지는 기존 문서상 미구현이며 이번에 구현하지 않았습니다.
- 범위: 서버 개발 환경의 요청된 마무리 점검 완료. 분석 프로그램 개발·주문·실거래·장기 운영 검증은 시작하지 않았습니다. 재부팅·리소스 변경·유료 API 호출·Commit·Push는 수행하지 않았습니다. ChatGPT는 요구사항 검토 역할, Codex CLI는 이번 서버 명령 실행·문서 기록·검증 역할이며 결과는 위 실제 도구 확인 범위에 한정됩니다.
- 오류: 기본 sandbox가 `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`로 명령 실행 전에 실패했습니다. 승인된 sandbox 외부 실행으로 점검했으며 sandbox 자체 문제는 해결하지 않았습니다.

기준일: 2026-11-10. 승인된 서버·네트워크 생성, developer 키 접속·sudo·SSH 보안·개발 도구·Clone·기본 환경 검증을 완료했습니다. 사용자 인증 로그인·앱 구현/운영은 미완료입니다. 아래 최신 결과 이후의 생성 전 조사·접속 대기는 당시 기록으로 보존합니다.

## 최종 개발 환경 구축·검증 결과

사용자 초기 스크립트 완료 보고 후 developer 노트북 키의 새 SSH 세션·sudo -n true를 도구로 검증했습니다. 콘솔 ED25519 지문과 고정 known_hosts를 사용하며 개인키는 노트북에만 유지했습니다. 콘솔 root 복구 접속은 사용자 확인 사실이고 root 계정·비밀번호는 변경하지 않았습니다.

SSH는 /etc/ssh/sshd_config.d/00-trading-key-only.conf에서 PubkeyAuthentication yes, PasswordAuthentication no, KbdInteractiveAuthentication no, PermitRootLogin no를 적용했습니다. 변경 전 설정은 root 전용 /var/lib/trading-setup/sshd-config-before-hardening.tar에 보관했습니다. sshd -t와 유효 설정, reload 후 새 developer 키 접속·sudo까지 검증했습니다. 포트·socket 활성화 구성을 변경하거나 ssh를 재설치하지 않았습니다. 복구는 콘솔 root 또는 검증된 sudo 경로로 설정을 점검·복원하며 새 세션 확인 전 기존 연결을 끊지 않습니다.

| 도구 | 실제 검증 버전 |
| --- | --- |
| OS | Ubuntu 24.04.1 LTS, x86_64 |
| Python / pip / venv | 3.12.3 / 24.0 / 생성·실행 성공 |
| Git / GitHub CLI | 2.43.0 / 2.45.0 |
| Node.js LTS / npm | 26.13.0 / 11.20.0 |
| 공식 Codex CLI | 0.167.0 |
| tmux / curl | 3.4 / 8.5.0 |

기본 도구는 Ubuntu 패키지의 python3-pip/python3-venv/git/gh/tmux/curl/ca-certificates/xz-utils로 설치했습니다. Node는 [공식 배포](https://nodejs.org/en/download)의 LTS linux-x64를 사용자 ~/.local/share/node에 설치하고 SHASUMS256.txt와 SHA256을 대조했습니다. node/npm/npx는 ~/.local/bin을 사용하며 Codex는 `npm install --global --prefix "$HOME/.local" @openai/codex@latest --no-audit --no-fund`로 설치했습니다. [공식 OpenAI 설치 안내](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)를 대조했으며 새 로그인에서도 PATH와 버전을 확인했습니다. 설치 명령의 latest는 향후 달라질 수 있어 이번 실제 버전을 위에 별도로 기록했습니다. 설치 로그는 ~/.local/state/trading-setup/install.log에만 보관했습니다.

`git clone --branch main --single-branch https://github.com/<OWNER>/<REPOSITORY>.git ~/trading-automation`로 main 8d2ddf1을 Clone했습니다. 문서 기록 전 원격 작업 폴더는 clean이었고 AGENTS.md·PROJECT_STATUS.md·NEXT_STEPS.md를 읽었습니다. AGENTS는 로컬과 CRLF/LF를 제외한 내용이 같습니다. 원격 Markdown 12개의 실제 bytes strict UTF-8·대체 문자·물음표 손상 검사를 통과했습니다. 합성 한글 JSON/로그의 쓰기·다시 읽기·JSON parsing과 Python venv 실행도 통과했으며 smoke 파일은 ~/.local/state/trading-setup 아래에만 있습니다. 콘솔 출력 인코딩 문제는 실제 파일 손상과 구분해 ASCII JSON으로 재검증했습니다.

메모리는 4,106,108,928 bytes, 루트 파일시스템 총 31,591,473,152 bytes, 도구 설치 후 여유 약 24.5GB였습니다. 할당된 CB1 30GB와 OS 표시·예약·사용량은 구분합니다. 런타임 검증은 개발 환경 smoke check이며 분석/주문 애플리케이션 구현·실행·성능 테스트가 아닙니다. 프로젝트 dependency manifest·framework가 없어 애플리케이션 자동 테스트 실행 대상은 없습니다.

GitHub·Codex 인증은 종료 코드만 확인했으며 둘 다 미로그인입니다. 사용자가 developer 세션에서 gh auth login 및 codex login --device-auth를 직접 수행합니다. [공식 headless 인증 안내](https://developers.openai.com/codex/auth/)를 따르며 계정의 device login 허용 여부는 미확인입니다. 로그인·유료 AI 호출은 하지 않았고 하루 4시간 자동 정지는 미구현입니다. 생성용 키 비활성화·정책 해지는 지금 사용자 콘솔에서 수행할 단계이며 아직 완료 미확인입니다. 아래 미완료·불일치·설치 대기 기록은 이전 단계의 이력입니다.

## 실제 생성 결과 및 초기 SSH 인계

### 후속 읽기 전용 SSH 경로 진단

### 최신 콘솔 지문 일치 및 초기 인증 인계

사용자가 수정해 제공한 콘솔 ED25519 SHA256 지문과 실제 대상에서 새로 수집한 공개키의 지문이 전체 문자열로 정확히 일치했습니다. 저장소 밖 전용 known_hosts에 해당 키만 등록했고 초기 접속 스크립트는 StrictHostKeyChecking=yes·ED25519로 고정했습니다. 자동 수락·호스트 키 검사 비활성화는 하지 않았습니다. 지문·IP·키 내용은 프로젝트 문서에 저장하지 않습니다.

초기 root 비밀번호는 사용자가 별도 PowerShell의 SSH 프롬프트에 직접 입력하도록 인계했습니다. 준비된 스크립트는 developer 계정의 노트북 Ed25519 공개키와 passwordless sudo를 설정하며 관리자 SSH는 유지합니다. 아직 사용자 실행 성공이나 일반 사용자 키 재접속·sudo는 검증되지 않았습니다. 이후 재접속·sudo·콘솔 복구 경로 검증 후 보안 강화·도구 설치·Clone을 진행합니다. 아래 불일치 기록은 이전 입력 시점이며 이번 일치 확인으로 신뢰 대조 중단 조건을 해소했습니다.

### 콘솔 지문과 실제 SSH 키 대조 — 불일치로 중단

사용자가 콘솔에서 확인한 ED25519 SHA256 지문을 제공했습니다. 실제 대상의 TCP 연결·SSH 배너는 확인됐으나 Windows ssh-keyscan은 `choose_kex: unsupported KEX method sntrup761x25519-sha512@openssh.com`으로 키 수집에 실패했습니다. 기존 Git for Windows의 ssh-keyscan으로 ED25519 키 1개를 수집하고 공개키 바이트의 SHA256을 직접 계산해 제공 지문과 전체 문자열을 대조했으며 **불일치**였습니다. [Windows OpenSSH 공식 이슈](https://github.com/PowerShell/Win32-OpenSSH/issues/2140)의 KEX 문제와 같은 오류이나 서버 SSH 설정은 변경하지 않았습니다.

사용자 지시대로 known_hosts 등록·비밀번호 인증·일반 사용자·SSH 강화·도구 설치·Clone은 중단했습니다. 호스트 키 검사 비활성화·자동 수락·기존 항목 삭제·서버 호스트 키 재생성은 하지 않았습니다. 콘솔에서 선택한 서버·ED25519 공개키 파일·지문을 다시 확인해야 하며 실제 지문·IP는 공개 프로젝트 문서에 기록하지 않습니다. 불일치 이유(전사 오류·다른 대상·키 교체 등)는 미확인입니다.

### 핫스팟 전환 후 승인된 SSH /32 교체

교체 후 Windows Test-NetConnection도 실제 대상 일치·TCP 22 TcpTestSucceeded=true로 성공했습니다. SSH 호스트 키 신뢰·로그인 성공과는 구분합니다.

사용자가 학교 Wi-Fi에서 휴대폰 핫스팟으로 전환하고 기존 SSH /32 교체를 승인했습니다. ipify의 새 공인 IPv4와 실제 서버 NIC의 ACG를 조회해 기존 학교 /32와 불일치를 확인했습니다. 기존 TCP 22 규칙 제거는 성공했고 직후 추가는 returnCode 1007009로 실패했습니다. 재조회로 ACG RUN·inbound 0개·outbound 5개를 확인한 뒤 현재 핫스팟 /32 추가를 한 차례 다시 수행해 성공했습니다. 최초 추가 실패의 상세 원인은 확정하지 않았으며 권한을 확대하지 않았습니다.

최종 재조회에서 TCP 22 inbound는 핫스팟 /32 규칙 1개, 기존 학교 규칙 없음, outbound 5개 유지가 확인됐습니다. 전체 인터넷 SSH를 개방하지 않았으며 로컬 private 입력의 SSH /32도 검증된 새 값으로 갱신했습니다. 직접 TCP 22 연결 및 SSH 배너 수신은 성공했습니다. 호스트 키의 신뢰 대조와 비밀번호 인증·일반 사용자 설정은 별도 단계이며 자동으로 신뢰하거나 진행하지 않습니다. 실제 IP·식별자는 저장소 밖에서만 관리합니다.

아래 학교 네트워크 진단은 각 시점의 기록입니다. 핫스팟에서의 성공만으로 기존 학교 네트워크의 차단 원인을 확정하지 않습니다.

최신 노트북 직접 대조: ipify에서 현재 노트북의 공인 IPv4를 새로 조회하고, 서버 조회에서 반환된 NIC 전체 1개와 그 NIC에 실제 연결된 ACG 1개의 inbound 규칙을 research-readonly로 조회했습니다. TCP 22 규칙 1개의 /32가 새 IPv4와 정확히 일치했습니다. 준비 파일의 과거 IP만 비교한 결과가 아니며 규칙 변경은 필요하지 않습니다. 실제 주소·리소스 식별자는 출력·기록하지 않았습니다. 추가 사용자 콘솔 확인은 BindIPv6Only=default·IPv4 TCP 22 LISTEN 있음·IPv6 LISTEN 없음입니다.

다음 최소 콘솔 점검은 아래와 같습니다. root 콘솔에서 방화벽을 읽기만 하며 출력은 콘솔에서만 검토합니다. 전체 ruleset·주소·로그를 채팅이나 저장소에 복사하지 않습니다. 도구가 없으면 설치하지 않고 부재로 기록합니다.

```bash
command -v ufw >/dev/null && ufw status verbose
command -v nft >/dev/null && nft list ruleset
```

패킷 도착 점검은 tcpdump가 이미 있을 때만 사용합니다. 콘솔에서 현재 노트북 IPv4를 로컬 프롬프트에 직접 입력해 해당 소스로 제한하고, 30초 동안 다른 노트북 PowerShell에서 TCP 22 검사를 한 번 실행합니다. 아래는 헤더의 SYN 패킷 개수만 출력하며 주소·페이로드·pcap 파일을 출력·저장하지 않습니다. 시작 시 Listening 또는 tcpdump 실행 오류는 로컬 콘솔에서만 확인합니다. any 인터페이스 중복 관찰·SYN 재전송 가능성이 있어 개수를 접속 횟수로 해석하지 않습니다.

```bash
if command -v tcpdump >/dev/null; then
  read -r -p 'Current laptop public IPv4 (local only): ' laptop_ipv4
  timeout 30 tcpdump -l -nn -i any "src host $laptop_ipv4 and tcp dst port 22 and tcp[tcpflags] & tcp-syn != 0" |
    awk 'END { print "SSH_SYN_packets=" NR }'
  unset laptop_ipv4
else
  printf '%s\n' 'tcpdump not installed; capture not performed'
fi
```

tcpdump 오류나 캡처 실패가 있으면 count=0을 미도착 증거로 사용하지 않습니다. 정상 캡처 중 정확한 소스의 테스트를 수행했는데 SYN=0이면 로컬/통신망·클라우드/게스트 수신 이전 경로를 계속 점검합니다. SYN>0이면 게스트까지 도착한 근거이므로 OS 방화벽·응답·소켓 서비스 활성화 실패 여부를 다음에 읽기 점검합니다. 두 경우 모두 SSH 설정 변경·재시작·재설치·재생성·전체 개방을 자동 수행하지 않습니다. [Ubuntu 제공 tcpdump 명령 설명](https://manpages.ubuntu.com/manpages/noble/man8/tcpdump.8.html)

최신 사용자 콘솔 확인: root 로그인 성공, system running, ssh.service inactive, ssh.socket active, TCP 22 LISTEN 1개, 직접 sshd -t는 /run/sshd 부재를 보고했습니다. 이는 사용자 확인 사항이며 도구가 OS에 로그인한 결과는 아닙니다. [Ubuntu 공식 소켓 활성화 설명](https://discourse.ubuntu.com/t/sshd-now-uses-socket-based-activation-ubuntu-22-10-and-later/30189/1)에 따라 연결 전 ssh.service inactive만으로 장애를 판단하지 않습니다. /run/sshd 부재도 단독 원인으로 확정하거나 디렉터리 생성·서비스 재시작·설정 변경·재설치로 대응하지 않았습니다.

콘솔 확인 후 현재 도구 재검사: 연결 대상 일치 상태에서 Windows Test-NetConnection TCP 22는 false, 직접 socket은 약 12초 TimeoutError입니다. SSH 배너·호스트 키 수집·인증·초기 설정은 진행하지 못했습니다. 콘솔에서 확인한 신뢰 지문은 아직 도구에 전달·비교된 상태가 아니며, TCP 성공 후 별도 콘솔 경로의 지문과 일치 검증을 선행합니다. 게스트 LISTEN의 IPv4 수신 가능 여부와 실제 패킷 도달·OS 방화벽·로컬 경로 원인은 미확인입니다. 다음 추가 읽기 점검은 콘솔에서 socket의 Listen/BindIPv6Only와 IPv4/IPv6 LISTEN, 게스트 방화벽·라우팅을 확인하는 것이며 변경하지 않습니다.

- research-readonly로 서버 RUN·operation NULL·event 0개를 재확인했습니다. 이는 하이퍼바이저/API 상태이며 OS 초기 부팅·cloud-init·SSH 서비스 완료의 근거는 아닙니다.
- 실제 서버에 연결된 Public IP와 저장소 밖 상태 파일·서버 목록의 Public IP 및 IP 인스턴스 연결이 모두 일치했습니다. api.ipify.org에서 재확인한 현재 사용자 IPv4는 입력 파일과 ACG의 /32에 일치했습니다. NIC에는 지정 ACG만 연결돼 있고 유일한 inbound는 현재 사용자 /32·TCP 22입니다.
- KR-1 Public Subnet의 VPC·기본 NACL 연결, 실제 Public Route Table 연관 Subnet, 기본 목적지의 Internet Gateway 경로를 재확인했습니다. 기본 NACL의 사용자 규칙은 0개입니다. [공식 NACL 설명](https://guide.ncloud-docs.com/docs/vpc-nacl-vpc)에 따르면 기본 허용이며 ACG는 stateful로 허용된 inbound의 응답을 자동 허용합니다. 조회된 클라우드 설정에서 SSH 차단 규칙은 발견하지 못했지만 실제 패킷 도달을 증명하지는 않습니다.
- Windows Test-NetConnection의 실제 대상 일치·TCP 22 검사 결과 TcpTestSucceeded=false입니다. 후속 직접 socket 검사는 12초 TimeoutError였습니다. 이전 10061 연결 거부와 이번 시간 초과를 구분하며 이를 sshd 미실행으로 단정하지 않습니다. 로컬/통신망 차단과 게스트 SSH·방화벽·부팅 문제는 아직 구분되지 않았습니다.
- connect-initial.ps1은 보호된 상태 파일의 실제 연결 Public IP, root 계정, 기본 포트 22를 사용합니다. ssh -G 유효 설정에서도 대상·포트·계정이 일치하며 ProxyCommand/ProxyJump가 없습니다. 비밀번호는 파일에 없고 호스트 키 확인을 요청하도록 구성돼 있습니다. 스크립트 실행·비밀번호 SSH 인증은 진행하지 않았습니다.
- 추가 API 권한은 필요하지 않았고 확대하지 않았습니다. 리소스·ACG·NACL·라우팅·계정·접속 스크립트는 변경하지 않았습니다. 서버 재생성·SSH 전체 공개·재부팅은 하지 않았습니다.
- 다음 단계는 사용자 메인 콘솔 `Korea·VPC > Server > youtube-analyzer > 서버 접속 콘솔`의 게스트 읽기 전용 점검입니다. 버튼이 활성화돼 있으면 직접 로그인해 아래 명령을 실행합니다. 비활성화돼 있으면 서버 콘솔 스크린샷으로 부팅/오류 화면만 확인하고, 콘솔 접근이 불가능한 경우 고객지원으로 게스트 접속 방법을 확인합니다. 기능 활성화를 위해 재부팅·권한 변경을 임의 수행하지 않습니다. [공식 원격 접속 오류 안내](https://guide.ncloud-docs.com/docs/server-ts-remote-lin-vpc)

```bash
systemctl is-system-running
cloud-init status
systemctl is-active ssh.service ssh.socket
/usr/sbin/sshd -t
ss -H -ltn 'sport = :22' | wc -l
/usr/sbin/sshd -T | awk '$1 == "port" { print }'
```

Ubuntu 24.04는 ssh.socket도 함께 확인합니다. 실패한 서비스·로그·게스트 라우팅·방화벽은 콘솔에서 직접 확인하되 실제 IP·전체 로그를 채팅이나 저장소로 복사하지 않습니다. 필요하면 `journalctl -b -u ssh.service -u ssh.socket --no-pager -n 50`, `ip route`, `ufw status`, `nft list ruleset`을 로컬 콘솔에서만 읽습니다. 기본 NCP 문제 해결 문서의 Ubuntu 예시는 18.04이므로 24.04 설정을 동일하다고 가정하지 않습니다.

TCP가 성공하면 콘솔에서 다음 공개 호스트 키의 SHA256 지문을 구하고 SSH 연결에서 제시하는 ED25519 지문과 직접 대조합니다. ssh-keyscan 결과만으로 신뢰하지 않습니다. 일치 확인 후 초기 로그인·developer 설정을 이어가며 일반 사용자 재접속·sudo·복구 검증 전 관리자 접근을 차단하지 않습니다.

```bash
ssh-keygen -E sha256 -lf /etc/ssh/ssh_host_ed25519_key.pub | awk '{print $2}'
```

- **사용자 확인:** provisioning 로컬 인증 준비 완료. 실제 계정·정책 설정 전체를 API로 감사한 결과는 아닙니다.
- **도구 검증:** 인증정보 출력 없이 조회 성공을 확인했습니다. 생성 직전 서버·VPC·Subnet·Public IP·Block Storage·Login Key·ACG 목록은 각각 0개였습니다. 이미지·스펙·CB1 30GB와 준비된 현재 사용자 IP /32 일치를 재확인했습니다.
- **생성·재조회 완료:** trading-vpc, KR-1 Public Subnet trading-public, 전용 ACG, Ncloud Login Key, youtube-analyzer 1대, CB1 기본 디스크 30GB 1개, Public IP 1개. 서버·IP는 RUN, 디스크는 ATTAC이며 소유 서버·VPC·Subnet·NIC·ACG 연결을 검증했습니다. c2-g3·2 vCPU·4GB·Ubuntu 24.04 이미지·KR-1 일치를 확인했습니다. 시간제 MTRAT로 요청했으며 목록 응답에는 요금제 필드가 없어 계정 청구 화면 재확인은 남아 있습니다.
- **네트워크:** 유일한 inbound는 TCP 22·준비된 사용자 IP /32입니다. outbound는 TCP 53/80/443, UDP 53/123만 허용했습니다. 기본 NACL 연결과 Public Route의 Internet Gateway 경로를 확인했습니다. NAT·Micro·추가 서버·추가 디스크는 생성하지 않았습니다. 식별자·IP·개인키는 저장소 밖 보호 파일로만 관리하며 research-readonly 인증·정책은 수정하지 않았습니다.
- **오류와 처리:** 서버 생성 직후 사양 검사 중단 후 생성 호출을 반복하지 않고 재조회해 승인 사양과 RUN 상태를 확인했습니다. getRouteList의 필수 vpcNo 누락 오류(returnCode 900)는 공식 인자를 보완한 조회로 해결했습니다. 이 오류를 권한 오류로 분류하지 않습니다. SSH TCP 22는 현재 실행 환경에서 ConnectionRefusedError(Windows 10061), 호스트 키 수집도 실패했습니다. 거부의 정확한 위치·원인은 미확인입니다.
- **초기 접속 경계:** View/getRootPassword는 준비 정책에서 제외돼 있어 권한 추가·비밀번호 API 호출을 하지 않았습니다. 사용자가 메인 콘솔 `Korea·VPC > Server > youtube-analyzer > 서버 관리 및 설정 변경 > 관리자 비밀번호 확인`에서 실제 Ncloud Login Key PEM으로 비밀번호를 직접 확인합니다. [공식 관리자 비밀번호 안내](https://guide.ncloud-docs.com/docs/server-manage-vpc#관리자-비밀번호-확인)를 따릅니다. 비밀번호·키를 채팅으로 받지 않습니다.
- **준비만 완료:** 저장소 밖에 별도 PowerShell용 초기 접속·developer 공개키 등록 스크립트를 준비했습니다. 호스트 키를 사용자가 확인하며 developer의 passwordless sudo를 설정하고 관리자 SSH 설정은 유지합니다. 아직 실행·검증되지 않았습니다. 먼저 일반 사용자 키 재접속·sudo·복구 경로를 검증한 뒤 SSH 보안을 강화합니다.
- **미실행·미검증:** 초기 SSH·호스트 키·일반 사용자·보안 강화, Python/pip/venv/Git/GitHub CLI/Node.js LTS/npm/공식 Codex CLI/tmux/curl 설치·버전, 서버 Clone·UTF-8·JSON·로그·OS 내부 메모리/디스크 점검. API 용량 검증과 OS 내부 점검은 구분합니다. 하루 4시간 자동 정지는 미구현입니다.
- **비용 추정:** 공개 단가 기준 운영 중 서버 92원+디스크 4.8원+IP 5.6원=102.4원/시간(VAT 별도), VAT 포함 단순 계산 112.64원/시간. 720시간 73,728원/VAT 포함 81,100.8원이며 지금도 보유·운영 비용이 발생합니다. 실제 청구·트래픽·현재 크레딧 잔액/VAT 처리는 미확인입니다. 가격·크레딧 권한은 확대하지 않았습니다.
- **키 회수:** 인프라 생성은 끝났으므로 SSH 인계 대기가 길면 사용자가 메인 콘솔에서 생성용 키를 비활성화하고 생성 정책을 해지합니다. SSH·도구 설치에는 생성용 API 키가 필요하지 않습니다. 최종 재조회는 research-readonly를 우선 사용합니다. 실제 키 비활성화·정책 해지 완료는 아직 미확인입니다.
- **AI 범위:** 도구가 승인된 실제 생성·재조회, 로컬 초기 접속 스크립트 준비·문서 기록을 수행했습니다. OS 구축 완료나 매매 성능으로 기록하지 않습니다. 기존 미커밋 변경·Git 이력을 보존하며 Commit·Push하지 않습니다. 애플리케이션 코드·framework가 없어 자동 테스트 실행 대상은 없습니다.

## 이전 생성 전 준비 기록

## infra-provisioner 설정 준비 — 이전 인계 지점

사용자는 별도 생성용 서브 계정·최소 권한 설정을 승인했습니다. 서버 생성 승인도 유효합니다. 기존 research-readonly 계정·정책·키를 수정하지 않습니다.

- 실제 확인: 기존 인증으로 공식 Sub Account 목록 GET을 한 번 호출했으며 HTTP403으로 거부됐습니다. 응답 전체·계정 식별자는 출력하지 않았고 재시도·계정/정책 생성 호출은 하지 않았습니다. 읽기 전제 확인 단계에서 막혔으므로 생성 권한의 개별 액션 거부를 확인했다고 주장하지 않습니다.
- 로컬 `provisioning` 프로필은 아직 없습니다. 기존 인증 파일의 작업 전후 바이트 해시 일치를 메모리에서 확인했으며 해시값·내용은 출력하지 않았습니다.
- 준비 완료: [사용자 정의 정책 JSON](infra-provisioner-policy.json). 공식 API의 policyName/description/permissions 스키마를 사용한 입력 자료이며 실제 원격 정책은 아닙니다. VPC10개·VPCServer29개 액션의 철자를 공식 권한 문서와 자동 대조했고 JSON 문법·중복·금지 액션 검사를 통과했습니다. 서비스 측 정책 유효성 검사·정책 할당·실제 실행 적합성은 인증 전이라 미검증입니다.

### 메인 콘솔 입력 순서

1. `Menu > All Services > Management & Governance > Sub Account > Policies > 정책 생성`으로 이동합니다. 이름은 `infra-provisioner-create`, 설명은 JSON의 description을 사용합니다. 관리형 정책을 선택하지 않습니다.
2. Visual 편집에서 `VPC` 및 `Server(VPC)`를 선택하고 각각 JSON의 `targets.product=VPC/VPCServer`에 있는 액션만 Allow로 추가합니다. JSON 전체는 공식 API 요청 본문 형태이므로 콘솔 편집기의 루트 형식과 혼동하지 않습니다. 콘솔 JSON 사용 시 정책 적용 대상의 permissions/effect/targets/actions/resourceNrns 구조를 확인합니다.
3. 자원이 아직 없으므로 `resourceNrns=["*"]`입니다. 이는 허용한 개별 액션의 리소스 범위이며 서비스 전체 액션 허용이 아닙니다. 이 정책만으로 KR-1·c2-g3·서버1대·SSH/32 조건까지 강제된다고 주장하지 않습니다. 승인 구성·개수·IP는 실행 전 로컬 입력과 조회 결과로 제한합니다. 미확인 조건 키·계정 번호는 만들어 넣지 않습니다.
4. 연관 액션이 자동 선택되면 준비 파일과 비교합니다. `Change/setSecondaryIP`, `Change/createPlacementGroup`, `Change/managePlacementGroupOfServerInstance`는 공식 서버 생성 연관 표에 있지만 이번 단일 기본NIC·Placement Group 없는 구성에서 사용하지 않아 제외했습니다. 삭제·반납·정지·재시작·NAT·IAM관리·전체 관리형 정책도 제외합니다. 이 제외로 콘솔 유효성 검사가 실패하면 오류 액션과 이유를 기록하고 멈추며 자동 추가하지 않습니다.
5. `Sub Account > Sub Accounts > 서브 계정 생성`으로 이동합니다. 로그인ID와 사용자명은 `infra-provisioner`, **콘솔 접근은 허용하지 않고 API Gateway 접근만 허용**합니다. API 접근 소스는 로컬 private 입력 파일의 현재 공인IP/32를 사용합니다. 오래된 IP인지 생성 직전 확인하고 실제 값은 프로젝트 문서에 넣지 않습니다. 콘솔이 비밀번호·사용자 정보를 요구하면 사용자가 해당 화면에서만 입력합니다.
6. 계정의 정책 탭에서 `[개별 권한 추가]`로 **이 사용자 정의 정책1개만** 연결합니다. 그룹/역할에서 다른 관리형·삭제 권한이 상속되지 않는지도 확인합니다. 기존 research-readonly의 정책이나 키는 건드리지 않습니다.
7. 사용자가 메인 콘솔의 해당 서브 계정 상세 `[Access Key]` 탭에서 API 키를 직접 생성합니다. 이후 별도 PowerShell에서 아래 인증 명령을 실행합니다. 키를 명령 인자·채팅·Git에 넣거나 인증 파일 내용을 출력하지 않습니다.

```powershell
Set-Location -LiteralPath '<NCLOUD_CLI_DIRECTORY> cli_windows'
.\ncloud.cmd configure --profile provisioning
```

기본 API URL은 `https://ncloud.apigw.ntruss.com`입니다. 기존 연구용 프로필을 다시 configure하지 않습니다. 콘솔 설정은 [서브 계정 안내](https://guide.ncloud-docs.com/docs/subaccount-use), [정책 편집 안내](https://guide.ncloud-docs.com/docs/subaccount-policy-role), 스키마는 [정책 검증 API](https://api.ncloud-docs.com/docs/management-subaccount-validatepolicy)를 근거로 준비했습니다. 키 생성·프로필 입력 완료 사실만 알려주면 다음 단계로 이어갑니다.

### 정책 범위와 알려진 경계

- VPC의 변경 액션은 VPC/Subnet 생성2개, Server(VPC)는 ACG생성·규칙설정·Login Key생성·서버생성·공인IP생성·연결6개입니다. 나머지는 공식 연관 조회 및 생성 결과 검증용 조회입니다. Route Table은 Public Subnet 연결 검증을 위한 조회만 허용하고 변경하지 않습니다.
- 공인IP 규칙의 액션명은 `View/getPublicIPDetail`, Login Key 목록은 `View/getLogInKeyList` 등 문서의 대소문자를 그대로 사용합니다. API 메서드 이름을 임의로 IAM 액션 이름으로 바꾸지 않았습니다. [VPC 권한 원문](https://guide.ncloud-docs.com/docs/networking-vpc-vpcetc), [Server 권한 원문](https://guide.ncloud-docs.com/docs/server-subaccount-vpc)
- `importLoginKey`의 별도 IAM 매핑은 미확인이라 추정 액션을 추가하지 않습니다. 준비한 일반 사용자 Ed25519 공개키는 유지하고, 초기 Ncloud Login Key는 문서에 있는 `Change/createLoginKey` 경로로 새로 생성해 반환 개인키를 로컬 보호 경로에만 저장하는 방식을 사용할 수 있습니다. 아직 실행하지 않았습니다.
- 초기 SSH에는 별도 경계가 있습니다. Ncloud Login Key는 관리자 비밀번호 암복호화용이며 OS의 일반 사용자 authorized_keys 설치를 자동 보장하지 않습니다. `View/getRootPassword`는 공식적으로 관리자 비밀번호 조회 액션이지만 **이번 생성·연결 정책에는 포함하지 않았습니다**. 필요하면 사용자가 메인 콘솔에서 초기 접속·일반 사용자 공개키 등록을 직접 수행하거나, 자동 초기 접속에 필요한 비밀번호 조회 범위를 구체적으로 설명한 뒤 별도로 처리해야 합니다. 조회 권한을 생성 권한에 숨겨 추가하지 않습니다. 관리자 접근은 일반 사용자 키의 새 세션 재접속 검증 전 차단하지 않습니다.

### 인증 완료 후 진행·실패·회수

- 사용자 입력 전에는 인증·계정·정책 생성 완료로 기록하지 않습니다. 인증 뒤 중복 리소스를 재조회하고 준비된 로컬/32의 최신성을 확인합니다. 승인된 상품·이미지·CB1 30GB·시간제·가격에 차이가 있으면 생성 전에 중단합니다. 이후 단계별 실제 결과를 검증하며 권한 거부는 반복하지 않습니다.
- 정책에는 삭제·반납이 없으므로 실패 시 자동 롤백하지 않습니다. 부분 생성된 서버/디스크/IP의 수·상태와 남는 시간당 비용을 보고하고, 삭제가 필요하면 사용자가 메인 콘솔에서 별도 처리합니다. 이번 실행은 계정·정책·자원을 생성하지 않아 이번 호출로 새로 발생한 자원 비용은 없습니다. 기존 원격자원 현황은 마지막 조회 기준과 구분합니다.
- 성공 시 일반 사용자 SSH 재접속, 개발 도구 설치·버전, Clone·UTF-8·JSON·로그 검증을 완료한 뒤, 마지막 필요한 인프라 검증과 실패 복구 여부까지 확인하고 **같은 작업 세션 종료 전에 생성용 Access Key를 사용자 메인 콘솔에서 비활성화**합니다. 이 작업은 아직 수행하지 않았습니다.
- 이후 `infra-provisioner-create` 정책을 해당 계정에서 해지해 생성 권한을 회수합니다. research-readonly는 유지합니다. 향후 인프라 변경 때만 별도 작업 기간 동안 다시 준비하며 키를 서버에 복사하거나 상시 활성 상태로 두지 않습니다. 아직 인증 전이므로 키 비활성화·권한 회수도 실행하지 않았습니다.

## 생성 전 승인용 후보 견적 — CB1 30GB

이 후보는 이후 사용자에게 **생성 승인**을 받았습니다. 다만 별도 생성용 인증이 발견되지 않아 원격 생성은 수행하지 않았습니다. 아래 견적은 승인된30GB 구성의 근거이며 실제 구축 완료 기록이 아닙니다.

| 항목 | 후보와 검증 상태 |
| --- | --- |
| 서버·OS | High CPU-g3 `c2-g3`, 2 vCPU·4GB, `ubuntu-24.04-base`(24.04 LTS) |
| 리전·존 | Korea VPC, KR-1 우선. 이미지별 스펙 조회 returnCode=0으로 호환 확인, 실제 재고 미검증 |
| 기본 디스크 | CB1 30GB. 해당 이미지 초기 크기10GB, KR-1·c2-g3·기본용 CB1 허용10~2000GB를 재조회(returnCode=0). 공식 생성 가이드의 KVM 용량 설정 조건을 만족하므로 API·문서상 선택 가능, 실제 생성 미검증 |
| 네트워크 | Public Subnet·Public IP1개, NAT Gateway 없음. VPC/Subnet/Route Table/ACG는 공식 안내상 무료 |
| SSH | TCP22를 사용자 접속 IP의 /32로 제한할 계획. 실제 IP 수집·저장·규칙 생성 없음 |
| 시간제 단가(VAT 별도) | 서버92원/시간, CB1 0.16원·GB/시간=30GB 4.8원/시간, Public IP5.6원/시간. 실행 합계102.4원/시간 |
| 정지 중 단가(VAT 별도) | 정지 할인 적용 시 서버 연산0원, 디스크4.8원+IP5.6원=10.4원/시간. 월중 디스크·IP 보유 가정 |

단가 출처: [공식 Korea 요금표](https://www.ncloud.com/charge/price/ko), [CB1 요금 설명](https://www.ncloud.com/api-cms/service-product/static/blockStorage), [VPC 무료 항목](https://www.ncloud.com/api-cms/service-product/static/vpc). 30GB 조건은 [서버 생성 가이드](https://guide.ncloud-docs.com/docs/server-create-vpc)와 CLI 조회를 대조했습니다. 가격 API는 이전 조회에서 권한 부족이었으므로 공개 요금 기반 참고 견적이며 계정별 확정 청구는 아닙니다.

| 30일 비용 | 상시 실행720시간 | 하루4시간 실행120시간·정지600시간 |
| --- | ---: | ---: |
| 서버 | 66,240원 | 11,040원 |
| CB1 30GB 보유720시간 | 3,456원 | 3,456원 |
| Public IP1개 보유720시간 | 4,032원 | 4,032원 |
| 통신 무료 범위 합계(VAT 별도) | **73,728원** | **18,528원** |
| VAT10% 단순 계산 | 7,372.8원 | 1,852.8원 |
| 크레딧 차감 전 VAT 포함 | **81,100.8원** | **20,380.8원** |
| 인터넷 송신100GB 예시 VAT 포함 | 89,900.8원 | 29,180.8원 |

비용 가정: 시간제·30일, 송신량은 실행 시간과 별개, 수신 무료·인터넷 송신 월20GB 무료량이 남아 있는 조건입니다. 20GB 초과~5TB는100원/GB이므로100GB 예시는8,000원(VAT 포함8,800원) 추가입니다. 다른 존·공인IP 경유 전송은 별도 조건입니다. 추가 스토리지·스냅샷·외부AI·관리형 서비스는 제외하며 실제 시간 올림·청구 절사에 따라 달라집니다.

정지 할인: High CPU-g3는 대상이나 OS 내부 shutdown만으로 할인 상태를 만족하는지는 미확인입니다. [공식 정지 안내](https://www.ncloud.com/support/faq/all/223)와 요금표의 1회 최대90일·12개월 누적180일 제한이 적용되며, 매일20시간 정지의 일수 산정은 미확인입니다. 정지600시간에도 디스크·IP비용6,240원이 남습니다(VAT 별도). 실제 정지 작업은 수행하지 않았습니다.

크레딧·Micro 조건:

- 사용자 확인 잔액100,000원·만료2027-02-28을 가정합니다. 다른 사용·트래픽이 없고 전 항목에 적용되며 VAT를 제외한 금액이 차감된다면 상시 약40.7일/하루4시간 약161.9일의 사용금액에 해당합니다. VAT까지 차감된다면 약37.0일/147.2일입니다. 이는 소진 상당 기간의 추정이며 청구 시점이나 무료 이용 기간 확정이 아닙니다.
- 2026-11-10부터 시작하는 예시에서 만료일까지 양 끝 날짜 포함111일이므로 하루4시간은 잔액보다 만료일이 먼저 제한할 수 있습니다. 실제 시작일이 늦거나 다른 사용이 있으면 기간이 달라집니다.
- **계정별 크레딧의 VAT 차감 가능 여부·할인 후 VAT 과세표준은 미확인**입니다. [Cost Analysis](https://guide.ncloud-docs.com/docs/costexplorer-costanalysis)는 크레딧 할인과 부가세를 별도 항목으로 계산하지만 이 정보만으로 VAT까지 크레딧으로 결제되는지 확정하지 않습니다. 따라서 VAT 포함 견적에서 크레딧100,000원을 단순 차감해 실청구0원으로 기록하지 않습니다.
- 소진·만료 뒤에도 보유·이용 자원에 일반 요금이 발생합니다. 크레딧을 자동 중지 장치로 간주하지 않습니다. 남은 청구액은 계정 결제 방식에 따라 납부되며, 실제 등록 수단·결제일은 미확인입니다. [일반 과금 원칙](https://www.ncloud.com/charge/price), [공식 결제 안내](https://www.ncloud.com/support/faq/all/1884)
- [무료 혜택 안내](https://www.ncloud.com/main/creditEvent)는 Micro1인1대·한국 거주·결제정보 등록 시점부터1년 무료와 이후 미반납 자동 과금을 안내합니다. [Server 사양](https://guide.ncloud-docs.com/docs/server-spec-vpc)상 Micro의 CB1/CB2 기본10GB까지 무료이며 추가 자원까지 모두 무료라는 뜻은 아닙니다.
- 해당 안내에는 크레딧 신청의 다른 할인 혜택 제한과 무료·체험 상품 결제 적용 제외도 있습니다. **이 계정의 기존 크레딧과 무료 Micro-g3를 병행할 자격·적용 우선순위는 미확인**으로 유지합니다. Micro를 생성하거나 기존 크레딧의 자격을 변경하지 않았습니다. 이 견적에는 Micro 비용·혜택을 합산하지 않습니다.

결정: 추가 트래픽·크레딧VAT 등 미확인 비용 조건을 고지한 상태로 사용자가30GB 구성 생성을 승인했습니다. research-readonly는 유지하며 별도 생성용 접근은 별도 준비·승인이 필요합니다. 인증정보·접속IP·리소스 식별자는 기록하지 않습니다.

## 생성 승인 후 실제 준비 결과와 콘솔 입력

- 검증됨: 이번 실행 직전 Korea·VPC의 VPC/Subnet/Server/Public IP/Block Storage/Login Key를 다시 조회했으며 각각 returnCode=0·totalRows=0입니다. KR-1의 Ubuntu24.04-base와 c2-g3 호환 및 CB1 30GB 허용 범위도 재확인했습니다. 상품·이미지·디스크 변경은 발견하지 않았습니다. 가격은 기존 공개 견적이며 계정별 확정 가격 조회 권한은 여전히 미확인입니다.
- 인증 준비 확인: 로컬 설정에는 research-readonly만 있고 다른 프로필·기본 인증·관련 환경변수 인증은 발견되지 않았습니다. **별도 생성용 인증 부재**가 중단 사유입니다. 프로필 이름만으로 실제 생성 권한 거부를 단정하지 않으며, 읽기 전용 프로필로 생성 호출을 시험하지 않았습니다. 403 생성 오류가 발생했다고 기록하지 않습니다. 기존 인증을 수정하거나 권한을 확대하지 않았습니다.
- 로컬 준비 완료: 저장소 밖 사용자 로컬 영역에 Ncloud 초기 인증키용RSA2048 PEM 키 쌍과 일반 사용자용Ed25519 키 쌍을 만들고 공개키 형식 검사를 통과했습니다. 전용 폴더는 현재 사용자와SYSTEM에만 접근하도록 ACL을 설정했습니다. 로컬 개인키는 passphrase 없이 생성하여 파일 ACL로 보호하며 저장소에 넣지 않았습니다. 공개키도 문서에 복사하지 않습니다.
- 외부 IPv4 조회 목적지 https://api.ipify.org 를 호출 전 사용자에게 알렸습니다. 현재 공인IPv4를 검증해 /32로 로컬 입력JSON에만 저장했습니다. 실제 IP·키·지문·사용자 계정 식별자는 출력하거나 프로젝트 문서에 넣지 않았습니다. VPN·네트워크 변경 시 생성/접속 직전에 다시 확인해야 합니다.
- 로컬 입력 파일: 사용자 로컬AppData의 `TradingAutomation/provisioning/youtube-analyzer-inputs.private.json`. 키 파일: 같은 로컬AppData의 `TradingAutomation/ssh/` 아래입니다. 파일의 정확한 로컬 경로는 작업 보고로만 안내합니다. private JSON의 문법과 /32 형식을 검증했습니다.
- 로컬 검증: ssh-keygen이 개인키 파일에 추가한 접근 항목을 확인했습니다. Set-Acl 방식은 SeSecurityPrivilege 오류로 실패했고, icacls로 해당 추가 허용 항목만 제거한 뒤 사용자/SYSTEM 제한과 개인키-공개키 일치를 재검증해 통과했습니다. 계정 보안 정책이나 클라우드 권한을 변경한 작업은 아닙니다.

콘솔은 Korea·VPC로 선택합니다. 아래 값은 실제 생성된 자원이 아니라 승인 범위의 입력값입니다. VPC와Subnet의 사설CIDR은 기존 KR 자원이 없는 상태에서 구현 기본값을 로컬 입력JSON에 정했고 아직 적용하지 않았습니다. 다른 VPN/사내망과 연동할 계획이면 충돌 여부를 먼저 확인합니다.

| 순서·콘솔 경로 | 입력값·선택 |
| --- | --- |
| Networking > VPC > VPC 생성 | 이름 `trading-vpc`; CIDR은 로컬JSON의 `vpc_cidr_proposed` |
| Networking > VPC > Subnet Management > Subnet 생성 | 이름 `trading-public`; VPC `trading-vpc`; KR-1; CIDR `subnet_cidr_proposed`; Internet Gateway `Y(Public)`; 용도 일반(`GEN`); 해당 VPC의Default NACL |
| Compute > Server > ACG 생성·설정 | 이름 `youtube-analyzer-ssh`; VPC `trading-vpc`; Inbound는TCP22, 출발지 로컬JSON의 `ssh_source_cidr`만 허용. Default ACG의 추가 허용 규칙을 함께 연결하지 않음 |
| ACG Outbound | 설치·조회에 필요한DNS(TCP/UDP53), HTTP/HTTPS(TCP80/443), 시간 동기화(UDP123)의 외부 통신 필요. 사용자 정의ACG는 기본 입출력 규칙이 없으므로 별도로 설정하고 확인. 실제 규칙은 미생성 |
| Compute > Server > 서버 생성 | OS이미지 KVM `ubuntu-24.04-base`, 서버 `c2-g3`, 2 vCPU·4GB, 1대, 이름 `youtube-analyzer`, KR-1, 시간제(`MTRAT`) |
| 서버 네트워크·스토리지 | `trading-vpc`/`trading-public`, eth0 사설IP 자동 할당, 위 전용ACG만 연결, 기본 디스크CB1 30GB, 추가 디스크 없음 |
| 초기 접속 인증키 | 이름 `youtube-analyzer-login-laptop`. 콘솔에서 새 인증키를 만들 경우 개인키는 사용자 로컬에만 다운로드. 준비한RSA 공개키 가져오기는 공식 importLoginKey API로 가능하나 콘솔 가져오기 UI·개별IAM매핑은 미확인으로 자동 실행하지 않음 |
| Compute > Server > Public IP | 1개만 생성해 `youtube-analyzer`에 할당. 서버 생성 단계에서 이미 할당했다면 추가 생성하지 않음. NAT Gateway·Micro·추가 유료 상품 없음 |
| 최종 확인 | Ubuntu24.04/c2-g3/CB1 30GB/시간제/공인IP1개와 기존 단가·견적을 대조. 다른 상품·OS·디스크·요금이면 생성하지 말고 중단 |

[VPC·Subnet 콘솔 절차](https://guide.ncloud-docs.com/docs/vpc-subnetmanage-vpc), [서버 생성 절차](https://guide.ncloud-docs.com/docs/server-create-vpc), [사용자 정의ACG 규칙](https://guide.ncloud-docs.com/docs/server-acg-vpc), [공개키 가져오기API](https://api.ncloud-docs.com/docs/compute-vserver-server-loginkey-importloginkey)를 확인했습니다. 콘솔 생성 최종 버튼도 유료 실행이므로 중복 목록과 값이 맞는지 다시 확인합니다.

### 생성 작업별 필요한 권한 — 별도 승인 전 변경 없음

관리자/전체서비스 정책 대신 아래 작업 범위와 공식 연관 조회 액션을 검토합니다. 이 표는 권한을 부여했다는 기록이 아닙니다.

| 서비스·작업 | 공식 문서의 액션과 연관 조회 |
| --- | --- |
| VPC 생성 | VPC의 `Change/createVPC`, `View/getVPCList` |
| Public Subnet 생성 | VPC의 `Change/createSubnet`, `View/getSubnetList`, `View/getNetworkACLList`, `View/getVPCDetail`, `View/getNetworkACLDetail`, `View/getVPCList` |
| 전용ACG 생성·규칙 설정 | Server(VPC)의 `Change/createACG`, `Change/setACGConfiguration`, `View/getACGList`, `View/getACGDetail`, `View/getVPCList`, `View/getVPCDetail` |
| 콘솔 초기 인증키 생성 | Server(VPC)의 `Change/createLoginKey`, `View/getLogInKeyList`. 공개키 import에 대한 개별권한 매핑은 별도 확인 필요 |
| 서버 생성 | Server(VPC)의 `Change/createServerInstance`와 공식 표의연관 액션. Server/ACG/InitScript/LoginKey/NetworkInterface/PlacementGroup/PublicIP/ServerImage/Storage/Subnet/VPC 조회 등이 포함되어 시각 편집기의자동 선택 목록을 확인할 것 |
| 공인IP 생성·할당 | Server(VPC)의 `Change/createPublicIPInstance`, `Change/associatePublicIPWithServerInstance`와 연관 Server/Storage/PlacementGroup/PublicIP 조회 |

서버 생성의 공식 연관 변경 액션에는 `Change/setSecondaryIP`, `Change/createPlacementGroup`, `Change/managePlacementGroupOfServerInstance`, 공인IP생성·할당도 나열되어 있습니다. 자동 선택된 연관 액션을 무조건 제거하거나 단순히서버생성 액션1개만으로 충분하다고 단정하지 않습니다. 실제 승인할 정책의 정확한JSON·범위는 콘솔에서 확인한 뒤 별도 접근 변경 승인을 받아야 하며, 현재 프로필에는 적용하지 않습니다. 삭제·정지·재시작·NAT·Micro 권한을 임의로 더하지 않습니다. [VPC 권한](https://guide.ncloud-docs.com/docs/networking-vpc-vpcetc), [Server 권한](https://guide.ncloud-docs.com/docs/server-subaccount-vpc)

### 서버 준비 뒤 남은 작업 — 미구현·미검증

- 일반 사용자 키 로그인을 설정한 뒤 기존 관리자 접속을 유지한 상태로 **새 SSH 세션 재접속**을 검증합니다. 이 검증 전 관리자 접근·암호 접근을 차단하지 않습니다. 관리자 비밀번호를 로그에 출력하거나 Git에 저장하지 않습니다.
- Python·venv·Git·GitHub CLI·Node.js LTS·npm·공식 Codex CLI·tmux·curl 설치·버전 검증은 원격 서버가 없어 수행하지 못했습니다. 저장소 Clone, UTF-8 파일 재읽기·JSON 파싱·로그 저장 검사도 미실행입니다. GitHub/Codex 인증 로그인은 사용자가 직접 수행합니다.
- 하루4시간 자동 정지·24시간 서비스 운영·유료AI API 호출·자동매매는 구현하거나 실행하지 않았습니다. 기존 미커밋 문서 변경을 보존하고 실제 완료된 로컬 준비와 원격 미실행을 구분합니다. Commit·Push는 하지 않습니다.

## 근거 구분

- 검증됨: 공식 CLI 1.1.30과 `research-readonly` 프로필의 조회 응답, 공식 문서의 사양·요금 조건.
- 사용자 확인: 별도 PowerShell의 서버 목록 조회 성공과 아래 콘솔 크레딧 정보.
- 추정: 공개 단가와 명시한 사용량을 대입한 비용. 실제 청구서·성능·생성 재고 검증이 아닙니다.
- 미확인: 가격·크레딧 API의 계정별 결과, g3a 단가·개별 정지 조건, g2 기본 디스크의 정지 단가 확정, 실제 재고·할당 한도·운영 성능.

## 기존 리소스 — 검증됨

| 대상 | CLI 서비스·액션 | 결과 |
| --- | --- | --- |
| Server | `vserver getServerInstanceList` | `returnCode=0`, `totalRows=0` |
| VPC | `vpc getVpcList` | `returnCode=0`, `totalRows=0` |
| Subnet | `vpc getSubnetList` | `returnCode=0`, `totalRows=0` |
| Public IP | `vserver getPublicIpInstanceList` | `returnCode=0`, `totalRows=0` |
| Block Storage | `vserver getBlockStorageInstanceList` | `returnCode=0`, `totalRows=0` |

공통 인자는 `--regionCode KR --profile research-readonly --output json`입니다. VPC 외 목록에는 `--pageNo 1 --pageSize 1000`도 지정했고 총수 0을 확인했습니다. 다른 리전·Classic·다른 서비스의 부재를 뜻하지 않습니다. 리소스명·IP·계정 및 리소스 번호는 기록하지 않았습니다.

## 2 vCPU·4GB 상품과 Ubuntu 호환성 — 검증된 카탈로그

| 상품 | 하이퍼바이저 | 호환 Ubuntu 이미지 | 기본 디스크 |
| --- | --- | --- | --- |
| `c2-g2-h50` | XEN | `ubuntu-20.04` 일반 이미지 상품 | HDD 50GB |
| `c2-g2-s50` | XEN | `ubuntu-20.04`, `ubuntu-20.04-64-server` 이미지 상품 | SSD 50GB |
| `c2-g3` | KVM·Intel | `ubuntu-22.04-base`, `ubuntu-24.04-base` | CB1/CB2, 최소 10GB |
| `c2-g3a` | KVM·AMD | `ubuntu-22.04-base`, `ubuntu-24.04-base` | CB1/CB2, 최소 10GB |

- KR-1·KR-2 모두 이미지별 상품·스펙 조회가 성공했습니다. 카탈로그 등재·호환성 확인이며 물리 재고·실제 생성 성공의 보장은 아닙니다.
- 전체 스펙 188개에는 g2 HDD/SSD 100GB 사양도 있으나, 이번 Ubuntu 20.04·50GB 이미지별 상품 조회에서는 50GB 사양만 반환되었습니다. 100GB 구성의 Ubuntu 호환성은 미확인입니다.
- 공식 Ubuntu 이미지 목록 3개 중 `ubuntu-22.04`는 BM용이며 대상 High CPU와의 호환 결과가 없었습니다. KVM의 `-base` 이미지와 구분합니다.
- Ubuntu 20.04 표준 보안 지원은 2025년 5월 종료, 22.04는 2027년 5월, 24.04는 2029년 5월까지입니다. 20.04의 Ubuntu Pro/ESM 적용·Ncloud 별도 지원은 미확인입니다. [Canonical 지원 기간](https://ubuntu.com/about/release-cycle)

## 기본 디스크 선택 조건

- `getBlockStorageVolumeTypeList`의 XEN 기본 디스크는 HDD·SSD, 기본 용량 50~100GB, 추가 볼륨 10~2000GB로 조회됐습니다.
- `--serverSpecCode c2-g3` 및 `c2-g3a`와 `--isBaseStorageAvailable true`를 지정하면 CB1·CB2만 반환됩니다. 기본 용량 10~2000GB, 추가 볼륨 10~16380GB이며 KR-1·KR-2에 대응합니다. 일반 가이드의 FB 계열을 이 사양의 기본 디스크 후보로 간주하지 않습니다.
- KVM Ubuntu 22.04/24.04 공식 이미지의 초기 매핑은 CB1·10GB입니다. CB2의 스펙 적합성은 확인했으나 실제 생성 조합은 검증하지 않았습니다.
- 10GB는 API상 최소 구성입니다. 영상 처리·임시 데이터에 충분하다는 뜻은 아니며 작업량·보관 기간을 측정한 뒤 용량을 결정합니다. 원본 영상은 공개 Git에 저장하지 않습니다.

## 요금 확인과 추정 비교

가격 API는 권한 부족으로 미조회입니다. 아래 단가는 [공식 Korea 요금표](https://www.ncloud.com/charge/region/ko)와 [Block Storage 공식 설명](https://www.ncloud.com/api-cms/service-product/static/blockStorage)의 참고값이며 적용 시점의 콘솔 견적 재확인이 필요합니다. 금액은 원(KRW)입니다.

| 항목 | 참고 단가·조건 |
| --- | --- |
| g2 HDD50GB | 96원/시간, 기본 디스크 포함 |
| g2 SSD50GB | 100원/시간, 기본 디스크 포함 |
| g3 | 92원/시간, 기본 디스크 별도 |
| g3a | 단가 미확인, g3와 같은 가격으로 간주하지 않음 |
| HDD/SSD | 0.08/0.16원·GB/시간. g2 정지 기본 디스크에 같은 단가가 적용되는지는 추정 |
| CB1/CB2 | 0.16원·GB/시간. 10GB 보유 1.6원/시간, 30일 1,152원 |
| Public IP | 개당 5.6원/시간, 30일 보유 4,032원 |
| 네트워크 | 수신 무료. 일반 인터넷 송신 월 20GB 이하 무료, 초과~5TB 100원/GB. 존 간·공인 IP 경유 전송 등은 별도 조건 |

추정 조건: 30일=720시간, 시간제, Ubuntu, Public IP 1개 월중 보유. 추가 디스크·스냅샷·NAT Gateway·Load Balancer 없음. 하루 4시간은 실행 120시간·정지 600시간으로 디스크·IP를 계속 보유합니다. VAT·크레딧 차감 전이며 실제 과금 시간 올림·청구 반올림은 반영하지 않았습니다.

| 구성 | 상시 30일 | 하루 4시간·30일 | 정지 중 시간당 잔여 비용(IP 포함) |
| --- | ---: | ---: | ---: |
| g2 HDD50GB | 73,152원 | 17,952원(정지 디스크 단가 조건부) | 9.6원(추정) |
| g2 SSD50GB | 76,032원 | 20,832원(동일 조건) | 13.6원(추정) |
| g3 CB1 10GB | 71,424원 | 16,224원 | 7.2원 |
| g3a CB1 10GB | `720R + 5184`원 | 정지 CPU 과금 0일 때 `120R + 5184`원 | CPU 정지 단가 미확인 |

`R`은 미확인인 g3a 서버 시간 단가입니다. 표의 금액에 통신비 `T`와 VAT를 더합니다. 일반 인터넷 송신만 월 20GB면 `T=0`, 100GB면 `T=8000`원인 예시입니다. 무료량이 다른 사용으로 소진되지 않았다는 가정이며 송신량이 운영 시간에 비례한다고 가정하지 않습니다. 외부 AI로 영상·음성을 보내면 송신이고 YouTube에서 받으면 수신입니다. 외부 AI API 요금은 비교에서 제외했습니다.

계산 예: g3 상시는 `92*720 + 0.16*10*720 + 5.6*720 = 71424`, 하루 4시간은 `92*120 + 0.16*10*720 + 5.6*720 = 16224`원입니다. g2 HDD 하루 4시간은 `96*120 + 4*600 + 5.6*720 = 17952`원으로 정지 기본 디스크 4원/시간을 가정했습니다. VAT10% 단순 합산 시 통신 무료 범위의 g3는 각각 약 78,566.4/17,846.4원이며 실제 청구·크레딧 적용 후 금액은 아닙니다.

- [공식 정지 요금 안내](https://www.ncloud.com/support/faq/all/223)와 공개 요금표에서 High CPU-g2/g3는 정지 할인 대상입니다. 기본 디스크·공인 IP·추가 스토리지는 정지 중에도 과금됩니다. g3a 개별 정지 조건은 미확인입니다. OS 내부 shutdown만으로 과금 정지 조건을 만족한다고 단정하지 않습니다.
- 정지 할인 대상에는 1회 최대 90일·12개월 누적 180일 제한이 있습니다. 매일 20시간 정지의 누적 일수 산정 방식은 미확인으로, 30일 비교를 무조건 연간으로 확장하지 않습니다.
- 최소 디스크 용량이 다른 비교입니다. g3도 CB1 50GB로 맞추면 디스크 월 5,760원, 상시 76,032원·하루 4시간 20,832원(통신·VAT 전)입니다. CPU 성능 비교는 수행하지 않았습니다.

## 크레딧과 권한 오류

- 사용자 콘솔 확인: 잔액 100,000원, 기간 2026-11-01~2027-02-28. Server(VPC), 기본 디스크, Block Storage, Public IP, Network - Server&LoadBalancer가 적용 목록에 포함됐습니다. 현재 잔액·적용 범위의 API 재검증은 미완료입니다.
- CLI 루트 도움말에 Billing 서비스가 없어 [공식 가격 GET API](https://api.ncloud-docs.com/docs/platform-listprice-getproductpricelist)와 [크레딧 GET API](https://api.ncloud-docs.com/docs/platform-discount-getcredithistorylist)를 같은 로컬 프로필로 호출했습니다. 인증정보는 메모리 내 서명에만 사용하고 값·인증 파일 내용·서명·전체 응답을 출력하거나 저장하지 않았습니다.
- 두 API 모두 HTTP403, `returnCode=2210`으로 각각 `View/getProductPriceList`, `View/getCreditHistoryList`의 권한 부족이 확인됐습니다. 네트워크 오류가 아니며 권한은 확대하지 않았습니다.
- [Credit 모델](https://api.ncloud-docs.com/docs/common-vapidatatype-credit)은 잔액·시작/종료 월·적용 가능한 상품 청구 유형을 제공합니다. 정확한 일 단위 만료일은 이 모델만으로 확인할 수 없습니다. 계정별 크레딧 이름·번호는 기록하지 않습니다.

## 재현·오류·검증 범위

- 저장소 밖 Windows CLI 1.1.30, 동봉 Java 1.8.0_41, Python 3.11.9의 임시 메모리 처리로 조회했습니다. CLI 배치가 상대 경로를 쓰므로 작업 디렉터리는 `cli_windows`로 지정합니다. 프로젝트 개발 환경 구축을 뜻하지 않습니다.
- 실행 전 `ncloud.cmd <service> <action> help --language en`으로 인자를 확인했습니다. 리소스 목록의 생 JSON은 출력하지 않고 `returnCode`·`totalRows`만 추출했습니다.
- 상품: `vserver getServerSpecList --regionCode KR`. KVM 이미지: `vserver getServerImageList --regionCode KR --osTypeCodeList UBUNTU --serverImageTypeCodeList NCP --platformCategoryCodeList OS --pageNo 1 --pageSize 1000`. g2 구형 이미지는 `getServerImageProductList`로 조회했습니다.
- KVM은 이미지 번호를 메모리 내에서만 `getServerSpecList --serverImageNo`에 전달하고 `--zoneCode KR-1/KR-2`로 대조했습니다. g2는 공개 이미지 상품 코드를 `getServerProductList --serverImageProductCode ... --generationCode G2`에 전달해 대조했습니다.
- 디스크: `vserver getBlockStorageVolumeTypeList --regionCode KR --serverSpecCode c2-g3 --isBaseStorageAvailable true`, g3a 및 `--hypervisorTypeCodeList XEN`도 별도 조회했습니다. 모든 명령에 공통 프로필·JSON 출력을 지정했습니다.
- 일부 초기 파싱 실패는 CLI 응답 CP949를 UTF-8로 읽은 문제였습니다. 엄격한 UTF-8/CP949 디코딩을 구분한 뒤 정상 파싱했습니다. 서비스 조회의 권한·네트워크 오류는 없었고 Billing API만 권한 부족입니다. 일부 공식 Web 본문은 타임아웃·404가 있어 공식 검색 결과·가이드로 보완했습니다.
- AI 작업은 조회·계산·기록입니다. 애플리케이션 테스트는 코드·framework가 없어 실행 대상이 없으며 서버 생성·접속·운영·성능은 미검증입니다.

## 다음 확인 항목

1. 권한은 유지하고 사용자 콘솔 확인으로 g3a 단가·g2 정지 기본 디스크 단가·크레딧 조건을 보완합니다. 키를 채팅에 전달할 필요는 없습니다.
2. Ubuntu 24.04의 g3/g3a는 검토 후보입니다. 디스크 용량·영상 작업량·외부 AI 비용을 설계해야 하며 아직 구성 선택·성능 검증을 완료하지 않았습니다.
3. 상품·구성·비용이 정해져도 실제 생성·변경은 별도 명시적 지시 후 진행합니다. 이번 조사에서는 Micro-g3도 생성하지 않았습니다.
