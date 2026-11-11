# 프로젝트 상태

## 2026-11-11 — 다른 컴퓨터 재개를 위한 통합 기록 확정

- 사용자가 다른 컴퓨터에서도 이어가기 위해 통합 문서의 Commit과 원격 보관을 요청했습니다. 문서 8개를 기준 b8e0854 위의 별도 docs 브랜치에서 검토·커밋하고 GitHub main에 일반 Push하는 범위입니다. 아래 Commit 금지·승인 대기는 이 요청 전의 기록입니다.
- 서버 통합 worktree의 공개 파일 24개를 기존 고정 호스트 키 SSH로 읽고 노트북에서 strict UTF-8·Markdown 14개 한글/손상/상대 링크/충돌 표시·실제 private 값 대조·Gitleaks 8.30.1 검사를 수행해 통과했습니다. 서버에 Gitleaks를 설치한 결과가 아니며 이 도구는 노트북에서 서버 파일의 실제 bytes를 검사했습니다. Commit 직전에는 실제 Git index와 staged diff를 다시 검사합니다.
- 문서만 바뀌었고 소스는 기존 b8e0854와 같아 테스트를 재실행하지 않습니다. 앞선 서버 Python 3.12.3 검증은 25개 통과·Windows 전용 1개 skip, 노트북 검증은 26개 통과입니다. ACG·SSH·권한·전원·실거래 변경은 없습니다.
- 원래 서버 main과 노트북의 dirty 작업 폴더는 보존합니다. 다른 컴퓨터에서는 GitHub main을 새로 Clone하거나 깨끗한 사본에서 fast-forward한 뒤 NEXT_STEPS.md와 docs/HANDOFF_2026-11-11.md를 읽습니다. 인증·개인키는 GitHub로 전달되지 않으며 새 기기는 별도 설정이 필요합니다.

## 2026-11-11 — 원격 최신 수신 및 서버 보존 통합

서버에서 원격 main을 fetch해 `b8e0854`를 직접 확인했습니다. 시작 main `fafae05` 대비 고유 커밋 0개·뒤처짐 2개이며 `1de8f6c`와 `b8e0854`를 별도 detached worktree에 반영했습니다. 기존 main의 미커밋 문서 7개와 HEAD·빈 index는 원래 폴더에 그대로 보존했고 저장소 밖 백업의 bytes·SHA256도 확인했습니다. 원래 main은 fast-forward하지 않았으며 최신 통합 검토 위치는 `../trading-automation-main-integration/`입니다. 이번 새 Commit·Push·staging은 없습니다.

노트북 후속 설치 완료는 전달된 설치 문서의 기록입니다. 코드 `1de8f6c`·기준 `b8e0854`의 소스 5개를 HEAD와 대조한 뒤 launcher·Python 모듈 총 4개를 배포했고, 각각의 기존 파일 백업 SHA256·설치 bytes 일치와 상태/입력/인증/공개키/개인키/known_hosts/SSH config 불변을 확인했다고 기록돼 있습니다. 설치 전 소스 dry-run·설치본 dry-run·VerifyOnly는 모두 add=false·remove_count=0이며, provisioning 명시 사용으로 실제 기본 NIC·지정 ACG 조회·TCP·고정 호스트 키의 developer 새 SSH 인증을 통과했다고 보고됐습니다. 서버가 이 배포·접속을 재검증한 것은 아닙니다. 아래 설치 대기 문구는 후속 설치 보고 전 시점입니다.

서버 직접 확인: 인계 폴더 `laptop-install-docs-ef5b3afa1968`의 HANDOFF·manifest·patch를 읽고 patch SHA256 및 문서 4개의 LF 정규화 기준/결과 SHA256을 확인했습니다. 기준 HEAD는 `b8e0854902add8d9d08a718fa6c01a11bc7ded32`입니다. 격리 기준 파일에서는 정방향·역방향 검사를 통과했고 현재 문서는 양방향 check 실패여서 강제 적용 없이 기존 기록에 수동 통합했습니다. 문서 diff 수신·검토 과제는 완료됐으며 노트북 미커밋 설치 기록이 GitHub에 올라갔음을 의미하지 않습니다. 이번에는 문서만 수정해 앱 테스트를 재실행하지 않았습니다.

서버 직접 검사: Python 3.12.3에서 `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py' -v` 실행, 26개 중 25개 통과·Windows OS byte lock 1개 skip. Windows PowerShell·Ruff 검사는 서버에서 실행하지 않았습니다. 노트북의 Windows 26개·lint·format·PowerShell·문서·민감정보 통과는 전달 기록입니다. 서버 문서 검사 결과와 범위는 [통합 안내](docs/HANDOFF_2026-11-11.md)를 따릅니다.

실제 핫스팟 전환 후 이전 관리 규칙 삭제·전용 ssh-acg 인증 준비·생성용 키 회수 확인은 남았습니다. 분석·주문 앱과 하루 4시간 자동 정지는 미구현입니다. 아래의 과거 소스 미수신·설치 대기·Commit 승인 지시는 현재 실행 지시가 아닙니다.

## 서버 앞선 대조 기록 — 원격 수신 전 시점

다음 추가 기록의 소스 미수신·동기화 대기·21개 테스트 문구는 원격 fetch 전 시점입니다. 최신 수신·26개 테스트 및 설치 전달 상태는 이 문서 상단과 통합 안내를 따릅니다. 11월 10일 기록은 원격에 이미 있어 재적용하지 않았습니다.

## 2026-11-11 — 서버 기록 대조 및 노트북 요약 통합

현재 우선 기록입니다. 아래 11월 10일 승인 대기·Commit 실패·미로그인·staged 보존 문구는 당시 단계의 이력이며 이번 실행 지시가 아닙니다. 이번에는 Commit·Push·staging을 하지 않습니다.

- 서버 직접 확인: 시작 HEAD `fafae055fd0be6eff603a48a9e41986c23e8fdfe` (`docs: finalize NAVER Cloud server setup records`), 작업 트리와 index 변경 없음, 추적 파일 14개. 로컬 커밋 존재만 확인했으며 이번 원격 조회·Push 여부 검증은 하지 않았습니다.
- 서버 파일 직접 확인: 기존 ChatGPT 로그인·venv·tmux와 IP 변경 복구 기록이 남아 있습니다. 이는 11월 10일 검증 이력이며 오늘 인증·접속을 재검증한 결과가 아닙니다. 기본 소켓 대상으로 `tmux list-sessions`를 실행했지만 소켓 부재 오류가 났습니다. 다른 소켓의 세션 유무는 미확인이고 종료·삭제는 하지 않았습니다.
- 인계 자료 직접 확인: 홈의 11월 10일 ZIP에는 HANDOFF·manifest·문서 4개용 패치만 있습니다. 오늘 SSH 도구 소스·테스트·의존성 파일은 서버 저장소와 확인한 ZIP에 없습니다. 과거 패치는 재적용하지 않았습니다.
- 사용자 제공 요약: 노트북에서 보관된 서버 기록을 통합하고 Windows SSH ACG 갱신 도구를 구현·설치·검증했다고 보고했습니다. 서버에서는 소스를 검토하거나 해당 검사를 재실행하지 않았습니다. 상세 동작·검증·제한과 필요한 전달물은 [통합 안내](docs/HANDOFF_2026-11-11.md)를 따릅니다.
- 완료 범위: 제공 요약의 근거 구분, 기존 서버 기록과 차이 정리, 다음 작업 정리. 최신 노트북 파일의 병합·양쪽 동기화는 자료 미수신으로 미완료입니다. 서버의 애플리케이션·테스트·의존성 도입 상태도 변경하지 않았습니다.
- 안전 경계: 인증 파일을 열거나 옮기지 않았고 클라우드·ACG·SSH·권한·서버 전원 변경, Windows 도구 설치·실환경 실행, 유료 API·실거래를 하지 않았습니다. 검사 결과와 실행 한계는 통합 안내에 기록합니다.

## 승인된 Commit·Push 완료 (2026-11-11)

- 사용자 승인 후 검토한 공개 변경 17개를 `1de8f6c` (`feat: refresh managed SSH access for changing public IPs`)로 커밋하고 GitHub main에 일반 Push했습니다. 기준 fafae05의 서버 구축 기록과 기존 이력을 보존했습니다.
- Commit 전 승인된 staged diff 해시 일치, 전체 index 23개 UTF-8·민감정보·private 값·Markdown 13개 링크·diff 검사 및 staged Gitleaks 탐지 0건을 재확인했습니다. 새 커밋을 포함한 전체 이력 10개 커밋도 Gitleaks 탐지 0건입니다. 코드 변경이 없어 앞선 unittest 26개·lint·format·PowerShell parse 결과를 유지하며 중복 실행하지 않았습니다.
- Push 직전 원격 main의 fafae05 유지를 확인했고 Push 후 검토 HEAD·origin/main·GitHub 원격 main의 1de8f6c 일치와 깨끗한 검토 worktree를 확인했습니다. 이 완료 결과는 별도 후속 문서 커밋으로 기록합니다.
- 원래 main의 HEAD 8d2ddf1·미커밋 파일 18개·빈 index는 그대로 보존했습니다. 원래 dirty main에서 pull하거나 reset·stash·강제 Push·Visibility 변경을 하지 않았습니다. 최신 작업은 별도 검토 worktree를 기준으로 합니다.
- 남은 작업: 검토본의 노트북 SSH 도구 재설치, 서버의 미커밋 변경 확인 후 원격 변경 통합, 전용 ssh-acg 인증과 생성용 키 회수 확인, 실제 핫스팟 전환·이전 관리 규칙 삭제 시험, 분석 최소 기능 설계·구현. 이번 승인 작업에서는 설치본·서버·ACG·인증을 변경하지 않았습니다.

아래 승인 대기·Commit 미실행 문구는 각 작업 당시 기록이며 이 완료 기록을 우선합니다.

## 최종 검토·커밋 준비 (2026-11-11)

- 최종 준비 완료: 공개 변경 17개를 검토 worktree index에 stage했습니다. 전체 index 23개 파일의 strict UTF-8·손상 문자·충돌 표시·실제 private 값·민감정보 검사와 Markdown 13개 상대 링크 검사, staged/working diff 검사를 통과했습니다. Gitleaks는 전체 이력 9개 커밋·작업 파일·index 전체 파일·staged diff에서 탐지 0건입니다. unittest 26개·Ruff lint/format·PowerShell parse 검사 통과, Git 작성자 설정도 값 출력 없이 준비 여부만 확인했습니다. 원래 작업 파일 18개·원래 HEAD·원래 빈 index 보존을 재확인했습니다. 탐지 0건은 해당 검사 범위의 결과입니다.

- 원격 확인: fetch로 main의 서버 구축 기록 커밋 fafae05를 확인했습니다. 원래 노트북 main은 8d2ddf1이며 미커밋 원본을 보존했습니다. 최신 원격 기준의 review/ssh-acg-20261111 브랜치·별도 worktree에서 오늘 변경을 통합합니다. reset·stash·이력 재작성은 하지 않았습니다.
- 통합 범위: 원격의 11월 10일 서버 현장 검증·종료·인계 기록을 기준으로 보존하고 오늘 노트북 기록·SSH 도구·테스트·사용 안내를 추가했습니다. 중복 상태 표와 이미 원격에 반영된 정책 JSON은 이번 변경에 재추가하지 않습니다. 원격 기록 통합과 현재 실행 중인 서버 파일 검증은 별개이며 후자는 이번 범위 밖입니다.
- 코드 검토: 동시 변경 시 예정 수량이 아닌 실제 수행한 규칙 추가·삭제를 집계하도록 수정하고 API·연결 실패 문구가 이미 성공한 삭제까지 복원했다고 오해되지 않도록 보완했습니다. Windows 전용 잠금 테스트는 다른 OS에서 명시적으로 skip합니다.
- 검사: Windows·Python 3.11.9에서 mock 테스트 26개 통과. 새 출력 집계·오류 안내 변경은 검토 worktree에만 있으며 기존 설치본을 재배포하거나 클라우드 규칙을 변경하지 않았습니다. 아래 실환경 검증은 앞선 설치본에서 수행한 결과입니다.
- 승인 경계: 이번 요청은 최종 검토·커밋 준비입니다. Git index에 공개 파일만 준비하고 staged bytes의 민감정보·UTF-8·링크·diff 검사를 수행합니다. 실제 Commit·Push와 원래 main의 작업 폴더 변경은 하지 않습니다.

이하 11월 11일 앞선 단계와 11월 10일 원격 기록은 당시 결과입니다. 현재 검토 결과는 이 절을 우선합니다.

## SSH ACG 자동 갱신 (2026-11-11 최신)

- 최종 확인: 설치본의 후속 dry-run·VerifyOnly 모두 add=false·삭제 0개이며 새 SSH 인증 재성공. 원래 상태·입력·인증·개인키·known_hosts bytes 불변을 확인했습니다. Markdown 13개 strict UTF-8·한글·손상 문자·상대 링크, 공개 후보 텍스트 22개 실제 private 대상 값 누출 검사, git diff --check 통과. Gitleaks 8.30.1 작업 파일 탐지 0건. staged 변경은 없습니다.

- 구현: scripts의 노트북 접속 도구·기기별 소유권 판별·저장소 밖 관리 기록·중복 실행 잠금, tests의 결정적 mock 테스트 21개, Ruff 설정과 고정 버전 개발 의존성을 추가했습니다. 분석·주문 앱은 여전히 미구현입니다.
- 실환경 확인: research-readonly 및 명시적으로 선택한 provisioning으로 dry-run 성공. 현재 공인 IPv4 `/32` TCP 22 새 규칙 추가 후 ACG·실제 기본 NIC 재조회·TCP 연결·StrictHostKeyChecking=yes developer 키 새 SSH 인증 성공. 삭제 예정 0개로 기존 식별 표시 없는 규칙을 보존했습니다. 서버 자동 시작·전체 개방·정책/인증 변경·API 키 서버 복사는 하지 않았습니다.
- 로컬 배포: 기존 connect-developer.ps1을 저장소 밖 날짜별 백업으로 보존하고 새 도구를 설치했습니다. 기존 provisioning 상태·입력·인증 파일 bytes 불변과 원본 백업 해시 일치를 확인했습니다. 기본 ssh-acg 전용 인증은 아직 준비되지 않았으며 자동 fallback은 없습니다. 현재 기존 인증 사용은 -Profile provisioning 명시가 필요합니다.
- 검증: Python 3.11.9·Windows의 unittest 21개, Ruff lint·format 검사 통과. 실제 다른 네트워크 전환·이전 관리 규칙 삭제는 미검증이며 mock 테스트만 통과했습니다. 기존 SSH 세션을 복원한 것이 아니라 새 연결을 검증했습니다. 서버 문서 통합은 별도 대기 상태입니다.
- 오류: sandbox의 패키지 조회·저장소 밖 잠금 접근 제한은 승인된 외부 실행으로 해결했습니다. PowerShell 실행 정책의 설치 차단은 영구 정책 변경 없이 자식 프로세스의 Bypass로 해결했습니다.
- AI 범위: 요구사항 검토와 로컬 파일 구현·mock 테스트·승인된 ACG 현재 IP 추가 및 새 접속 검증입니다. 공개 문서·로그에 실제 IP·ID·키를 남기지 않았고 Commit·Push는 하지 않았습니다. 사용·전용 인증·tmux 안내는 docs/SSH_ACCESS.md를 따릅니다.

## 작업 기록 통합 (2026-11-11)

- 로컬 검사: Markdown 12개 strict UTF-8·한글·손상 문자·상대 링크 검사, 보관 서버 점검 절 4개 항목 보존 검사와 git diff --check 통과. Gitleaks 8.30.1 작업 폴더 탐지 0건. 앱 코드 변경이 없어 애플리케이션 테스트 대상은 없습니다. staged 변경은 없습니다.
- 도구 오류: 최초 비교 출력의 cp949 인코딩 오류는 PYTHONIOENCODING=utf-8로 해결했습니다. PowerShell 파이프의 한글 스크립트 전달 실패는 파일 변경 전 중단됐고 UTF-8 스크립트 파일 실행으로 통합했습니다. 실제 문서 bytes 검사를 통과했습니다.

- 로컬 통합 완료: 2026-11-10 서버 문서 보관본의 마무리 점검 절을 네 문서에 추가했습니다. 노트북의 SSH 접속 복구 기록과 기존 이력은 보존했습니다.
- 당시 서버 도구 확인: Codex ChatGPT 로그인, 임시 venv 생성·실행·환경 분리, 격리 tmux 접속·분리·동일 pane 재접속 성공. GitHub CLI 인증은 해당 점검 범위 밖이므로 미확인입니다. 아래 과거 Codex 미로그인 문구보다 후속 로그인 확인 기록을 우선합니다.
- 오늘 확인: 고정 호스트 키와 키 인증 설정을 유지한 SSH 시도는 sandbox에서 연결 거부, 승인된 외부 재시도에서는 시간 초과였습니다. 사용자는 서버를 아직 열지 않았다고 알렸습니다. 서버 RUN 여부와 접속 불가 원인은 오늘 도구로 확인하지 못했습니다.
- 서버 반영 대기: 현재 서버 파일·미커밋 변경·인증 상태를 읽거나 수정하지 못했습니다. 양쪽 동기화는 미완료입니다. 서버 접속 후 최신 문서와 대조해 통합해야 하며 기존 인계 패치도 적용 검사가 필요합니다.
- 다음 작업: 서버 기동·SSH 접속 확인 → 서버 최신 문서와 로컬 통합본 비교 → 서버 고유 변경 보존·추가 내용 반영 → UTF-8·diff·민감정보 검사. Codex 재로그인은 상태 확인 결과 필요할 때만 수행합니다. 생성용 키·정책 회수와 GitHub 인증은 별도 확인 대상입니다.
- AI 작업 범위: 보관 문서 비교와 로컬 기록 통합입니다. 앱 구현·유료 호출·클라우드 설정 변경·Commit·Push는 수행하지 않았습니다.

## Commit 작성자 설정 오류 및 해결 (2026-11-10)

사용자 승인 후 최종 7개 파일을 stage하고 전체 14개 파일의 UTF-8·한글·손상·상대 링크 검사, 작업 파일·index·staged diff Gitleaks 탐지 0건 및 diff 검사를 통과했습니다. Commit은 서버의 Git user.name·user.email 미설정으로 실패해 새 커밋이 생성되지 않았으며 Push는 실행하지 않았습니다. 사용자가 기존 main 마지막 커밋 작성자 사용을 승인해 해당 정보를 저장소 로컬 Git 설정에만 적용했습니다. 작성자 값은 문서에 복사하지 않았습니다. 변경을 보존한 뒤 승인된 Commit·Push를 이어갑니다. 생성용 키 회수·GitHub 인증·현재 크레딧은 미확인입니다.

## Commit·Push 승인 및 최종 반영 준비 (2026-11-10)

사용자가 통합된 변경 전체의 Commit·Push를 승인했습니다. 기존 승인 대기·unstaged 보존 기록은 승인 전 단계의 이력입니다. 문서 6개와 공개 정책 예시 1개의 최종 통합분을 명시적으로 stage하고 UTF-8·링크·민감정보·diff 검사를 다시 수행한 뒤 일반 Commit·Push합니다. 원격 main fetch 후 기준 HEAD 8d2ddf1 대비 앞섬/뒤처짐 0/0을 확인했습니다. 생성용 키 회수·현재 크레딧·실제 청구와 GitHub CLI 로그인 상태는 재검증하지 않았습니다.

## 노트북 추가 인계: 접속 IP 변경 복구 (2026-11-10)

근거: 전달 ZIP의 `HANDOFF.txt`와 추가 전용 패치를 이번 서버 세션에서 직접 읽었습니다. 아래 접속 복구 검증은 노트북 측 도구 결과의 전달 기록이며 이번 서버 세션에서 클라우드 변경이나 접속 시험을 재실행한 결과가 아닙니다. 노트북 원본 작업 폴더는 직접 확인하지 않았습니다.

- 최신 developer 타임아웃 복구: 연구용 조회에서 서버 RUN·Public IP 연결·실제 NIC ACG를 확인하고 ipify의 새 노트북 IPv4와 기존 SSH /32 불일치를 확인했습니다. 유효한 provisioning 권한으로 이전 TCP 22 /32 제거 후 ACG 비동기 반영 완료(RUN)를 재조회하고 현재 /32 규칙 1개로 교체했습니다. 이전 규칙 제거·outbound 5개 유지를 확인했고 Test-NetConnection true, 기존 고정 호스트 키의 developer 새 세션·sudo 검증이 성공했습니다. 전체 공개·권한 확대·SSH 재설치·재생성·Commit·Push는 하지 않았습니다.

## 오늘 종료 상태 (2026-11-10)

오늘 범위인 NAVER Cloud 영상 분석 서버와 개발 환경 구축을 완료했습니다. 분석·자동매매 프로그램 개발은 시작하지 않았습니다. 기존 현장 도구 검증 기록, 사용자가 이번에 전달한 완료 사실과 이번 문서 점검 결과를 구분합니다. 최초 정리 시 노트북 자료는 미전달이었으나 후속 전달 ZIP의 HANDOFF·manifest·패치는 직접 검토하고 적용했습니다. 노트북 원본 파일을 직접 확인한 것은 아닙니다.

- 기존 도구 검증: 읽기 전용 인증·생성 전 자원 부재·g2/g3와 Ubuntu 및 비용 비교, 승인 후 생성용 최소 정책 준비·인프라 생성, developer 키 인증·sudo·SSH 강화·도구 설치·Clone·UTF-8/한글 JSON/로그/자원·ChatGPT 로그인·tmux 생성/접속/분리/동일 pane 재접속. 세부 근거는 [서버 기록](infrastructure/NAVER_CLOUD.md)을 따릅니다.
- 사용자 확인: 실제 SSH 종료 후 developer 재접속·sudo 검증 완료. 이는 기존 tmux의 PTY 시험과 별도 근거이며 재부팅 후 검증을 의미하지 않습니다. 콘솔 root 복구 경로는 유지했습니다.
- 사용자 콘솔 자료: 크레딧 100,000원, 2026-11-01~2027-02-28, 적용 상품 확인. 현재 잔액 재조회는 하지 않았습니다. Public 저장소 확인은 기존 도구 기록이며 이번에는 원격 main fetch 후 HEAD·origin/main `8d2ddf1`, 앞섬/뒤처짐 0/0을 직접 확인했습니다.
- 추정 비용: 30일 상시 VAT 포함 약 81,101원, 하루 4시간 약 20,381원. 디스크·Public IP는 중지 중에도 과금됩니다. 가격·크레딧 API 권한 부족, 크레딧 VAT·무료 Micro 병행 조건은 미확인입니다. 공식 출처·가정은 서버 문서에 보존했습니다.
- 미완료: 분석·자동매매 개발, 4시간 자동 정지, Remote-SSH 실제 연결, 데스크톱 별도 키, 재부팅 후 접속·장기 운영, 백업 실행·복구, 비용 알림, 생성용 API 키 비활성화·정책 해제 완료 확인.
- 유료 AI API는 호출하지 않았습니다. Codex 구독 로그인 기반 분석은 향후 검증 계획이며 로그인 성공을 분석 기능 검증으로 취급하지 않습니다.
- 이번 Codex 작업은 기존 파일 보존·문서 통합·Git 및 파일 검사입니다. 서버 중지·재부팅·리소스 변경·Commit·Push는 수행하지 않습니다. ChatGPT의 요구사항·설계 검토와 Codex CLI의 파일 수정·명령 실행·검증 역할을 구분합니다.

## 서버 현장 마무리 점검 (2026-11-10)

직접 검증한 도구 버전·venv·sudo·ChatGPT 로그인·tmux 결과와 당시 오류는 [서버 현장 점검 기록](infrastructure/NAVER_CLOUD.md)에 통합했습니다. 아래 과거 미로그인·접속 대기 문구는 단계별 이력입니다. 최신 상태는 이 문서 상단 종료 기록을 따릅니다.

기준일: 2026-11-10. 사용자 확인, 도구 검증과 계획을 구분합니다.

| 항목 | 상태 | 근거 및 남은 작업 |
| --- | --- | --- |
| 기본 문서 및 폴더 | 생성 완료 | Markdown12개·.gitignore·생성용정책JSON. 애플리케이션 코드·의존성 명세·빌드 설정·자동 테스트 없음 |
| GitHub 초기 구축·Public 전환 | 완료·검증됨 | 사용자 전환·접근 확인 보고 후 GitHub 도구로 Public·기본 브랜치 main 재확인, 기존 커밋 6개 보존 |
| 노트북 작업 환경 | 사용자 확인 완료 | Windows 노트북에서 Git·GitHub CLI·Codex CLI 설치·인증·Clone·실행 완료 |
| main 동기화 | 직접 검증됨 | 사용자 승인 후 문서 커밋 811d8e0 일반 Push 완료, 로컬 main·origin/main·GitHub API 원격 main 일치 확인 |
| 공개 개발 문서 | 반영·Push 완료 | Public 전환 기록 811d8e0 반영, 이후 완료 결과 기록을 별도 커밋으로 보존 |
| Python 개발 환경 | 미설정 | 프로젝트 지원 런타임·의존성·포매터·린터·테스트 도구 선정 및 명령 검증 필요 |
| 유튜브 분석 시스템 | 계획·미구현 | 아키텍처, 영상 목록·자막 수집, AI 전략 추출, Markdown·JSON 스키마 설계 필요 |
| 네이버 클라우드 서버 | 개발 환경 구축·검증 완료 | 승인 사양 유지. developer 키 재접속·sudo·SSH 강화·도구 설치·Clone·UTF-8/JSON/로그/자원 검증 완료. 인증 로그인·앱 운영 미검증 |
| Binance Futures 주문 프로그램 | 미구현 | 분석과 분리된 주문 기능 설계 예정 |
| 백테스트·모의매매·위험 관리 | 미구현 | 실거래 전 위험 한도·복구까지 검증 필요 |
| 24시간 운영·매매 성능 | 미검증 | 실행·운영·성과 측정 근거 없음 |

## 환경과 확인 범위

- 개인 Windows 데스크톱에서 시작한 프로젝트를 현재 Windows 노트북에서 이어서 작업합니다. 노트북 설치·로그인·Clone·Codex CLI 실행 완료는 사용자 확인 사항입니다.
- 이번 환경에서 Git 2.56.0.windows.4, GitHub CLI 2.103.3, Python 3.11.9 실행을 확인했습니다. Python 설치 확인은 프로젝트 개발 환경 구성 완료를 의미하지 않습니다.
- 사용자가 Public 전환과 정상 접근을 확인했다고 보고했습니다. 이번 작업에서 GitHub 도구로 visibility=public·default_branch=main과 main 브랜치 존재를 재확인하고, GitHub CLI API로 원격 main의 4df4bf7 일치를 확인했습니다. 이번 작업에서 Visibility를 변경하지 않았습니다.
- 사용자 콘솔 확인 크레딧은 100,000원, 2026-11-01~2027-02-28이며 적용 목록은 infrastructure/NAVER_CLOUD.md에 기록했습니다. API 재검증은 권한 부족으로 미완료입니다. 공개 단가 기반 추정 비용과 계정별 확정 요금을 구분합니다.
- 과거 데스크톱의 CLI 오류를 현재 노트북 문제로 단정하지 않습니다.

## 이전 검증 및 보존 기록

- 과거 한글이 실제 물음표로 손상된 문서 11개를 확인된 문맥에 따라 재작성했습니다. 원문 복원이 아니며 관련 이력은 보존합니다.
- 사용자 제공 이전 보안 감사 결과: 전체 커밋 5개와 작업 파일 Gitleaks 탐지 0건, 인증정보·개인정보 유출 미발견, Issues·PR·Actions·Releases 등 확인 완료. 연결된 GitHub Projects 없음은 사용자 직접 확인 사항입니다.
- 탐지 0건은 사용한 검사 범위의 결과이며 모든 위험 부재의 증명은 아닙니다. 이번 검사 결과는 아래 최신 검증 기록에 구분합니다.

## 이전 공개 준비 작업 (4df4bf7에 반영됨)

- .gitignore에 로컬 인증 설정, DB·저널·백업, analysis/raw/ 규칙을 추가하고 SQL 소스·공개 예시·fixture 처리 기준을 명시했습니다.
- 공개 개발 규칙, AI 활용 범위, 외부 자료 권리 확인, 설계 결정 이유, staged content 검사와 Push 전 diff 확인 절차를 문서화했습니다.
- 서버·분석·주문 프로그램은 완료로 변경하지 않았습니다. 애플리케이션 테스트는 코드와 framework가 없어 실행 대상이 없습니다.
- 아래는 이전 작업 당시의 검사·승인 대기 기록입니다. 해당 변경은 현재 로컬·원격 main의 4df4bf7에 포함되어 있습니다. 이번 문서 변경의 승인 상태는 NEXT_STEPS.md와 최신 검증 기록을 따릅니다.

## 이전 공개 준비 검증 기록 (당시 Commit 전)

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

## Public 전환 완료 및 최신 검증 기록 (2026-11-10)

- 사용자 확인: Public 전환·정상 접근 완료. 도구 확인: GitHub visibility=public, 기본 브랜치 main, main 브랜치 존재. GitHub CLI API 원격 main·로컬 main·origin/main은 4df4bf7로 일치하며 기존 커밋 6개를 보존했습니다.
- 변경 범위: README.md, PROJECT_STATUS.md, NEXT_STEPS.md, CHANGELOG.md. 공개 상태와 이전 기록의 시점을 구분했습니다. AGENTS.md의 보안·AI 활용·테스트 기록 규칙은 계속 적용합니다. 새 설계 결정은 없습니다.
- 작업 파일과 Git index의 Markdown 각 12개: 실제 bytes의 엄격한 UTF-8 디코딩·한글 존재·대체 문자·연속 물음표·대표 손상 패턴·상대 링크 검사 통과. 전체 13개 파일의 작업 내용·index 내용에서 개인키·토큰·인증정보 대입·이메일·IPv4 보조 패턴 탐지 0건입니다.
- 기존 임시 도구 Gitleaks 8.30.1로 전체 이력 6개·작업 파일·index 전체 13개 파일·staged diff 검사 탐지 0건. `git diff --check`와 `git diff --cached --check` 통과. 검사 범위의 결과이며 모든 민감정보 부재를 보증하지 않습니다.
- 재현 명령: 이전 임시 도구를 PATH에 추가한 환경에서 `gitleaks git . --log-opts="--all --full-history" --redact --no-banner`, `gitleaks dir . --redact --no-banner`, `gitleaks git . --pre-commit --staged --redact --no-banner`. index 전체 검사는 `git show :경로`의 bytes를 저장소 밖 임시 폴더로 추출해 `gitleaks dir`로 검사했습니다. 추출 파일은 검사 후 자동 정리했습니다.
- 오류 및 처리: GitHub CLI API 최초 조회의 sandbox 네트워크 제한과 Git index 쓰기 제한은 승인된 재실행으로 해결했습니다. LF→CRLF 안내는 줄바꿈 정규화 경고이며 UTF-8 손상은 확인되지 않았습니다.
- AI 작업 범위는 공개 상태 확인·문서 수정·검증 기록입니다. 애플리케이션 테스트는 코드·framework가 없어 실행 대상이 없으며 서버·실거래·성능은 미검증입니다.
- 위 검사는 Commit 전 결과입니다. 이후 사용자 승인으로 문서 4개를 811d8e0 (`docs: record public repository transition`)으로 Commit하고 main에 일반 Push했습니다. 새 커밋 포함 전체 이력 7개 Gitleaks 탐지 0건, Push 직전 변경 파일·diff 및 원격 main의 4df4bf7 유지를 확인했습니다.
- Push 후 GitHub API 원격 main·로컬 main·origin/main의 811d8e0 일치, 깨끗한 작업 폴더 및 Public·기본 브랜치 main 유지를 확인했습니다. 이 완료 결과는 후속 문서 커밋으로 기록합니다. Visibility 변경·이력 재작성·강제 Push는 수행하지 않았습니다.

## 최신 서버 생성 결과 (2026-11-10)

### 개발 사용자·SSH 보안·도구·Clone 최종 검증

- 사용자 확인: 초기 접속 스크립트 완료, 서버 콘솔 root 복구 접속 성공. 도구 검증: developer 노트북 Ed25519 키의 새 세션 재접속과 sudo -n true 성공. 개인키는 노트북 밖으로 복사하지 않았습니다. 다른 기기 공개키는 제공되지 않아 설치하지 않았습니다.
- SSH 보안: 설정 백업 후 키 인증 유지, PasswordAuthentication/KbdInteractiveAuthentication/PermitRootLogin을 no로 설정하고 sshd -t·유효 설정 검사·reload·새 developer 세션·sudo 검증을 통과했습니다. 기존 세션을 먼저 차단하지 않았고 콘솔 root 계정·비밀번호는 변경하지 않았습니다. 복구 콘솔 성공은 사용자 확인이며 자동 재접속 시험은 아닙니다.
- Ubuntu 24.04.1 LTS x86_64에서 Python 3.12.3·pip 24.0·venv 생성, Git 2.43.0·GitHub CLI 2.45.0·Node.js LTS 26.13.0·npm 11.20.0·Codex CLI 0.167.0·tmux 3.4·curl 8.5.0을 검증했습니다. Node는 공식 배포 파일의 SHA256 대조, Codex는 공식 @openai/codex npm 패키지를 사용했습니다. 새 로그인 PATH에서도 node/npm/codex 실행을 확인했습니다.
- developer의 ~/trading-automation에 main(8d2ddf1)을 Clone하고 원격 AGENTS.md·상태 문서를 읽었습니다. AGENTS는 로컬과 CRLF/LF를 제외한 내용이 일치합니다. 원격 Markdown 12개의 strict UTF-8·손상 문자 검사, 저장소 밖 합성 한글 JSON·로그 round-trip과 venv 실행을 통과했습니다. 문서 출력의 콘솔 인코딩 문제는 ASCII JSON·실제 bytes 검사로 구분했으며 원문 파일 손상은 없었습니다.
- OS 내부 메모리 4,106,108,928 bytes, 루트 파일시스템 총 31,591,473,152 bytes, 도구 설치 후 여유 약 24.5GB를 확인했습니다. API의 4GB/30GB 상품 용량과 OS 표시·사용량 차이를 구분합니다.
- 오류 처리: 첫 SSH 보안 스크립트의 Windows 텍스트 줄바꿈 전송 실패는 변경 전 상태를 읽어 확인한 뒤 UTF-8 bytes/LF 전송으로 해결했습니다. AGENTS 원시 바이트 해시 불일치는 CRLF/LF 차이였으며 줄바꿈 정규화 후 내용 일치를 확인했습니다.
- 미완료: GitHub·Codex 인증은 종료 코드만 확인해 각각 미로그인입니다. 로그인·유료 AI 호출·앱 실행은 하지 않았습니다. 분석/주문 코드·framework가 없어 애플리케이션 자동 테스트 대상이 없고 하루 4시간 자동 정지는 미구현입니다. 생성용 키 비활성화·정책 해지는 사용자가 콘솔에서 수행해야 하며 완료 미확인입니다. 아래 접속 대기·지문 불일치·미설치 기록은 이전 단계의 이력입니다.

- 호스트 키 고정 후 developer 노트북 키의 비대화형 재접속·sudo를 한 차례 검사했으나 publickey 인증이 거부됐습니다(SSH 255, 호스트 키 오류 없음). 사용자 초기 설정 스크립트 완료 보고가 없어 일반 사용자·sudo 검증은 대기입니다. 비밀번호를 요청·수집하거나 API로 조회하지 않았습니다.
- 최신 지문 확인: 사용자가 다시 제공한 콘솔 지문과 실제 SSH 대상에서 새로 수집한 ED25519 키의 SHA256 전체 문자열이 정확히 일치했습니다. 저장소 밖 전용 known_hosts에 해당 키만 등록하고 초기 접속 스크립트를 StrictHostKeyChecking=yes로 준비했습니다. 비밀번호는 사용자 별도 PowerShell의 SSH 프롬프트에서만 입력합니다. developer 공개키·passwordless sudo 설정과 관리자 접근 유지는 준비됐으나 스크립트 실행·일반 사용자 재접속·sudo는 아직 미검증입니다. 아래 불일치 기록은 이전 입력 시점의 기록입니다.
- 네 번째 제공 지문은 길이도 한 글자 짧고 실제 수집 지문과 불일치했습니다. known_hosts 미생성·인증 미시도 상태를 재확인했습니다. 콘솔 출력 원문을 직접 복사해 재확인하는 단계이며 원격 변경은 없습니다.
- 세 번째 제공 지문도 실제 ED25519 키 재수집과 대조한 결과 한 글자 불일치했습니다. known_hosts 미생성·인증 미시도 상태를 확인하고 중단을 유지했습니다. 신뢰 콘솔에서 해당 글자를 다시 확인해야 합니다.
- 사용자가 수정해 제공한 두 번째 콘솔 지문도 실제 ED25519 키를 새로 수집해 대조한 결과 불일치했습니다. known_hosts 등록·접속 중단을 유지했고 실제 수집 지문은 사용자 응답에만 표시해 콘솔 재확인을 요청합니다. 지문을 프로젝트 문서에 저장하지 않았습니다.
- 최신 보안 중단: 사용자가 콘솔 ED25519 지문을 제공해 실제 SSH 대상 키와 SHA256 전체 문자열을 대조했으나 불일치했습니다. known_hosts 등록·인증·일반 사용자 설정·도구 설치·Clone을 중단했습니다. Windows ssh-keyscan의 unsupported KEX 오류는 기존 Git 제공 수집 도구로 공개키를 읽어 해결했으며 서버 설정은 변경하지 않았습니다. 사용자 콘솔의 대상 서버와 ED25519 공개키 지문을 다시 확인해야 합니다. 지문·실제 IP·개인키는 프로젝트 문서에 기록하지 않으며 호스트 키 검사를 비활성화하지 않았습니다.
- 핫스팟 교체 후 Windows Test-NetConnection에서도 대상 일치·TCP 22 TcpTestSucceeded=true를 확인했습니다. 이는 연결 경로 검증이며 호스트 키 신뢰·로그인 성공을 의미하지 않습니다.
- 최신 핫스팟 전환: 사용자의 명시적 교체 승인 후 ipify 새 IPv4와 실제 NIC ACG를 비교해 학교 /32와 불일치를 확인했습니다. 학교 TCP 22 규칙 제거 후 최초 추가는 1007009로 실패했으나 상태 재조회(ACG RUN·inbound 0개) 후 한 차례 추가에 성공했습니다. 최종 inbound는 현재 핫스팟 /32 TCP 22 한 규칙이며 학교 규칙은 없고 outbound는 유지됐습니다. 직접 TCP 연결·SSH 배너 수신 성공, 호스트 키 신뢰 확인·인증은 대기입니다. 권한 확대·SSH 서비스 변경·전체 공개·재생성·Commit·Push는 하지 않았습니다. 아래 네트워크 진단은 이전 시점 기록입니다.
- 최신 노트북 검증: ipify의 새 공인 IPv4와 서버가 반환한 실제 NIC 1개→연결 ACG 1개→TCP 22 inbound 규칙의 /32를 직접 대조해 정확한 일치를 확인했습니다. 준비 파일의 과거 IP만 비교하지 않았고 규칙 변경은 필요하지 않습니다. 사용자 확인인 BindIPv6Only=default·IPv4 LISTEN 있음·IPv6 LISTEN 없음도 구분해 기록했습니다. 콘솔의 OS 방화벽 읽기·해당 노트북 소스 SYN 개수 확인 명령만 준비했으며 실제 캡처·방화벽 점검은 아직 미실행입니다.
- 최신 사용자 콘솔 확인: root 로그인·system running·ssh.socket active·TCP 22 LISTEN 1개, ssh.service inactive 및 sshd -t의 /run/sshd 부재. 소켓 활성화를 고려해 서비스 장애로 단정하지 않았습니다. 이후 도구 재검사는 Test-NetConnection false·직접 socket 약 12초 시간 초과였습니다. 호스트 키·인증·일반 사용자 설정은 여전히 미검증이며 SSH 설정 변경·재시작·재설치·디렉터리 생성은 하지 않았습니다. 사용자 콘솔 확인과 도구 검증을 구분하며 실제 외부 경로 원인은 미확인입니다.
- 후속 읽기 전용 진단: research-readonly로 RUN·operation NULL, 실제 Public IP 연결, 현재 공인 IP와 ACG /32, NIC·Public Subnet·기본 NACL·실제 Route Table 연관·IGW 경로 및 접속 스크립트 대상/root/22 일치를 재확인했습니다. 기본 NACL 사용자 규칙은 0개이며 공식 기본 허용 조건과 대조했습니다. Windows Test-NetConnection TCP 22는 false, 후속 socket은 12초 시간 초과입니다. 이전 10061과 구분하며 게스트 초기 부팅·SSH 서비스·정확한 차단 위치는 미확인입니다. 추가 권한·원격 변경·인증·재생성 없이 사용자 서버 접속 콘솔의 읽기 전용 서비스/부팅 점검과 별도 경로 호스트 키 확인 절차를 준비했습니다.
- 사용자 확인: provisioning 로컬 인증 준비 완료. 도구 확인: 조회 인증 성공·기존 7종 목록 0개·승인 사양·현재 SSH /32 재확인 후 순차 생성했습니다.
- 생성 검증: trading-vpc/trading-public·전용 ACG·Ncloud Login Key·youtube-analyzer(c2-g3, 2 vCPU·4GB, Ubuntu 24.04, KR-1)·CB1 기본 디스크 30GB·Public IP 1개. 최종 서버/디스크/IP 각 1개, 소유·연결 관계와 RUN/ATTAC 상태를 확인했습니다. MTRAT로 요청했고 응답에 요금제 필드가 없어 청구 화면 재확인은 남았습니다.
- 보안: SSH inbound는 현재 사용자 IP /32의 TCP 22 한 규칙이며 NAT·Micro·추가 자원·유료 AI는 사용하지 않았습니다. 식별자·개인키·IP는 저장소 밖에서 관리하고 research-readonly는 변경하지 않았습니다.
- 오류: 생성 직후 검사 중단은 재생성 없이 조회로 해결했고 Route 조회의 필수 vpcNo 누락(returnCode 900)도 보완했습니다. SSH는 연결 거부(Windows 10061), 호스트 키 수집 실패로 최초 접속·원인·OS 설정은 미검증입니다. 비밀번호 조회 권한을 추가하거나 해당 API를 호출하지 않았습니다.
- 인계: 사용자 메인 콘솔의 관리자 비밀번호 확인과 별도 PowerShell용 로컬 초기 설정 스크립트를 준비했습니다. developer 공개키·passwordless sudo 설정은 아직 미실행입니다. 키 재접속·sudo·복구 경로 검증 전 관리자 접근은 유지합니다. 개발 도구·Clone·서버 UTF-8/JSON/로그/OS 자원 점검·SSH 강화는 미실행입니다.
- 비용: 운영 중 공개 단가 기준 시간당 VAT 별도 102.4원·포함 112.64원, 720시간 포함 81,100.8원 추정입니다. 현재도 비용이 발생하며 실제 청구·트래픽·현재 크레딧 잔액/VAT는 미확인입니다. 자동 정지는 미구현입니다.
- 인프라 생성 종료 후 SSH 인계 대기가 길면 사용자가 생성용 키 비활성화·정책 해지를 수행하도록 안내합니다. SSH에는 생성용 API 키가 필요 없고 최종 재조회는 연구용 프로필을 우선합니다. 회수 완료는 아직 미확인입니다.
- AI 작업 범위는 승인된 생성·재조회·접속 스크립트 준비·문서 기록입니다. 기존 미커밋 변경·Git 이력 보존, Commit·Push 없음. 애플리케이션 자동 테스트는 코드·framework가 없어 실행 대상이 없습니다. 상세 근거는 infrastructure/NAVER_CLOUD.md를 따릅니다.
- 로컬 검사: Markdown 12개 strict UTF-8·한글·대체 문자·연속 물음표·상대 링크 검사 통과, 정책 JSON의 product별 상품별 중복 없는 액션 총 39개 확인, 실제 로컬 키·리소스 식별자·IP와의 대조 탐지 0건, 작업 폴더 Gitleaks 탐지 0건, git diff --check 통과. staged 파일은 0개이며 index는 변경하지 않았습니다. 초기 스크립트의 PowerShell 구문·bash -n 검사만 통과했고 실제 원격 실행은 미검증입니다. 제한 환경의 Git Bash 시작 실패는 허용된 환경에서 문법 검사로 재확인했습니다.

## 이전 네이버 클라우드 읽기 전용 조사 (2026-11-10)

다음 인증 미설정·미생성 문구는 이전 작업 당시의 기록이며 현재 상태는 위 최신 결과를 따릅니다.

최신 인증 준비: 사용자가 별도 infra-provisioner/API Gateway 전용 계정·최소 권한 설정을 승인했습니다. 현재 인증의 Sub Account 목록 GET 1회가 HTTP403으로 거부돼 추가IAM호출·계정/정책생성은 수행하지 않았습니다. provisioning프로필은 아직 없으며 기존인증파일의 전후 바이트불변을 확인했습니다. infrastructure/infra-provisioner-policy.json에 공식 이름의39개 개별액션을 준비·대조했고 삭제/반납/전체관리/IAM/보조IP/PlacementGroup변경은 제외했습니다. 메인콘솔 설정·사용자직접키생성·로컬인증·구축후키비활성화/정책해지 시점을 NAVER_CLOUD.md에 기록했습니다. 정책서비스검증·할당·원격생성·SSH/개발도구설치는 미실행입니다. 초기관리자비밀번호조회는 생성정책에 포함하지 않았으며 필요한접속절차와권한경계를 명시했습니다.

최신 생성 승인 후 결과: youtube-analyzer 1대·c2-g3·Ubuntu24.04·KR-1·CB1 30GB·공인IP1개·trading-vpc/trading-public·NAT없음·SSH사용자IP/32 구성을 사용자가 명시적으로 승인했습니다. 원격6종 목록은 다시0개였고 이미지·스펙·30GB범위를 재검증했습니다. 로컬에는research-readonly만 있으며 별도 생성 인증이 발견되지 않아 원격 생성은 미실행입니다. 생성 권한의403거부를 관찰한 것은 아니며 읽기 전용프로필로쓰기호출을시험하지 않았습니다. 로컬 전용ACL 폴더에RSA/Ed25519키와현재/32입력JSON을 준비·검증하고 콘솔 입력·필요권한을 infrastructure/NAVER_CLOUD.md에 기록했습니다. 원격 도구 설치·Clone·UTF-8/JSON/로그 검사·일반사용자재접속은 서버가 없어 미실행입니다. 하루4시간자동정지도 미구현입니다. 권한 확대·Micro생성·유료AI호출·Commit·Push는 하지 않았습니다.

최신 후보 견적: 사용자가 지정한 KR-1·High CPU-g3(2 vCPU·4GB)·Ubuntu24.04·CB1 30GB·Public IP1개·Public Subnet·NAT 없음입니다. 이미지 호환성과 기본용 CB1 범위10~2000GB를 읽기 전용 재조회하고 생성 가이드와 대조해30GB 허용 조건을 확인했습니다. 실제 생성은 미검증입니다. 공개 단가 추정은 상시73,728원/하루4시간18,528원(VAT 별도), VAT 포함81,100.8원/20,380.8원입니다. 크레딧VAT·무료Micro 병행은 미확인이며 상세 승인용 표는 infrastructure/NAVER_CLOUD.md를 따릅니다. 생성·권한 변경·Commit·Push는 하지 않았습니다.

- 사용자 확인: 별도 PowerShell에서 research-readonly 프로필로 Korea·VPC 서버 조회 성공, 0개 보고. 이번 도구 조회로도 서버·VPC·Subnet·Public IP·Block Storage 각각 returnCode=0·totalRows=0을 확인했습니다. 다른 리전·Classic까지 조회한 결과는 아닙니다.
- 검증됨: 공식 Windows CLI 1.1.30의 도움말로 명령·인자를 확인하고 실행했습니다. KR-1/KR-2에서 2 vCPU·4GB의 g2 HDD/SSD50GB와 Ubuntu20.04, g3/g3a와 Ubuntu22.04/24.04의 카탈로그 호환성을 확인했습니다. 기본 디스크는 XEN 최소50GB, 대상 KVM 사양 최소10GB CB1/CB2입니다. 생성 재고·성능은 미검증입니다.
- 검증됨: 가격·크레딧 GET API는 HTTP403·returnCode=2210으로 각각 조회 권한 부족입니다. 네트워크 오류와 구분했으며 권한을 확대하지 않았습니다. CLI 응답 일부의 CP949 디코딩 문제는 UTF-8/CP949 엄격 디코딩 분기로 해결했습니다.
- 추정: 공개 단가·30일·시간제·IP1개 보유·통신 무료 범위에서 g3 CB1 10GB는 상시71,424원·하루4시간16,224원(VAT 전). g2 정지 디스크 단가 적용은 조건부, g3a 단가·개별 정지 조건은 미확인입니다. 같은 용량 비교·통신100GB 예시·정지 중 비용은 infrastructure/NAVER_CLOUD.md에 기록했습니다.
- AI 범위: 조회·계산·문서 기록이며 서버·Micro-g3·권한 생성/변경/삭제는 수행하지 않았습니다. 인증정보·실제 리소스 식별자·전체 응답은 기록하지 않았습니다. 애플리케이션 테스트는 코드·framework가 없어 실행 대상 없음입니다.
- 문서 검증: Markdown12개의 실제 bytes 엄격한 UTF-8·한글·손상 문자·상대 링크 검사 통과. 변경5개 파일의 보조 민감정보 패턴 검사와 git diff --check 통과, Gitleaks8.30.1 작업 폴더 검사 탐지0건입니다. staged 변경은 없으며 이번 변경은 Commit·Push하지 않습니다. 다음 단계는 미확인 가격·크레딧 조건과 용량·작업량 설계의 보완입니다.

## GitHub 반영 준비 검사 (2026-11-10)

- 작업 파일 및 Git index 전체 14개 파일(Markdown 12개): 실제 bytes strict UTF-8·한글 존재·대체 문자·연속 물음표·상대 링크 검사 통과. 정책 JSON은 상품별 중복 없는 액션 총 39개, 삭제·중지·재부팅·비밀번호 조회 액션 제외 확인.
- Gitleaks 8.30.1 공식 릴리스 SHA256 대조 후 작업 파일·index 전체 파일·staged diff 탐지 0건. `git diff --check`, `git diff --cached --check` 통과. 검사 범위의 결과이며 전체 위험 부재를 보증하지 않습니다.
- 보조 검사: 개인키·토큰·실제 IPv4·이메일·개인 Windows 경로 후보 검사. OpenSSH KEX 이름의 `@openssh.com`은 이메일 패턴 후보였으나 공개 알고리즘 식별자로 확인해 해당 문자열만 예외 처리했습니다. 그 밖의 후보는 없습니다. 기존 개인 Windows CLI 경로는 placeholder로 바꿨습니다.
- 검토·stage 대상: CHANGELOG.md, NEXT_STEPS.md, PROJECT_STATUS.md, README.md, docs/DECISIONS.md, infrastructure/NAVER_CLOUD.md, infrastructure/infra-provisioner-policy.json. 인증 설정·임시 파일·로그·원본 영상은 포함하지 않았습니다. 검사 스크립트·도구·index 추출물은 저장소 밖 /tmp에만 준비했습니다.
- 재현: `gitleaks dir . --redact --no-banner`, `gitleaks git . --pre-commit --staged --redact --no-banner`. 전체 index는 `git show :<PATH>`의 실제 bytes를 임시 디렉터리에 추출해 별도로 검사했습니다.
- 기존 로컬 변경·정책 예시는 보존하며 검토한 7개 파일만 명시적으로 stage했습니다. 애플리케이션 코드·framework가 없어 앱 자동 테스트 실행 대상은 없습니다. 서버 재검증·리소스 변경은 이번 범위에 없습니다.
- 오류: 기본 sandbox의 bwrap loopback 권한 오류로 실행이 실패해 승인된 외부 실행을 사용했습니다. Gitleaks PATH 부재는 /tmp 도구 준비로 해결했습니다. 정책 검사의 최초 전역 중복 조건은 서로 다른 상품의 같은 액션명을 중복으로 판단해 실패했으며, 상품별 고유 액션 검사로 정정해 통과했습니다. 원격 main fetch 결과 HEAD·origin/main 8d2ddf1, 앞섬/뒤처짐 0/0입니다. Commit·Push·Visibility 변경은 하지 않았으며 사용자 승인 대기입니다.

## 전달 패치 통합 검사 (2026-11-10)

- 홈의 전달 ZIP을 저장소 밖 /tmp에 안전 경로·symlink 검사 후 해제했습니다. HANDOFF.txt를 읽고 manifest의 HANDOFF·패치 SHA256 일치를 확인했습니다. ZIP·인계 파일·검사 도구는 저장소에 추가하지 않았습니다.
- 패치 내용은 문서 4개에 접속 IP 변경 복구 기록 25줄 추가, 삭제 없음입니다. 현재 작업 트리에서 `git apply --check`를 두 차례 통과한 뒤 일반 `git apply`로 적용했습니다. 충돌·강제 적용·3way·reset·stash·전체 파일 덮어쓰기는 없었습니다.
- 전달 근거: 새 공인 IP와 기존 SSH /32 불일치 확인, 승인된 기존 규칙 제거, ACG RUN 반영 확인 후 새 /32 추가, inbound 1개·이전 규칙 없음·outbound 5개 유지, TCP 검사·기존 신뢰 호스트 키의 developer 새 세션·sudo 성공. 이번 서버 세션에서 해당 작업을 재실행한 것은 아닙니다.
- 생성용 키 회수·정책 해제 완료, GitHub 인증의 현재 상태, 현재 크레딧·실제 청구는 미확인으로 유지합니다. 과거 콘솔 크레딧 자료는 당시 확인 이력입니다. 기존 ChatGPT 로그인·venv·tmux 검증 기록은 보존했습니다.
- 통합 후 작업 파일·기존 index 전체 14개(Markdown 12개)의 strict UTF-8·한글·손상 문자·상대 링크·보조 민감정보 검사 통과. 전달 파일·작업 파일·index 전체·기존 staged diff Gitleaks 탐지 0건, 일반 및 cached diff --check 통과.
- 기존 index의 staged diff는 통합 전후 바이트 단위로 동일합니다. 이번 패치·문서 통합은 문서 4개와 의사결정 기록의 unstaged 변경으로 유지하여 기존 staged 작업과 구분했습니다. 승인 전 최종 통합 내용을 다시 검토·stage해야 합니다. 앞선 staging 완료 기록은 이번 추가 통합 전의 결과입니다.
- 분석·주문 개발, 유료 AI API 호출, 서버 리소스 변경·중지·재부팅·Commit·Push는 수행하지 않았습니다.
