# 핫스팟 IP 변경 시 SSH 접속

## 구현과 검증 범위

Windows PowerShell 5.1과 Python 3.11.9에서 검증한 노트북용 도구입니다. 실행 코드는 `scripts/`, 결정적 mock 테스트는 `tests/test_ssh_acg.py`에 있습니다. 분석·주문 앱의 개발 환경을 설정한 것은 아닙니다.

`scripts/connect-developer.ps1`은 ipify 공인 IPv4 검증 → 서버 RUN·고정 대상 확인 → 기본 NIC에 연결된 지정 ACG 확인 → 규칙 비교 → 필요한 경우 현재 `/32` TCP 22 추가 → ACG RUN 재조회·규칙 존재 확인 → TCP 및 기존 developer 키·고정 호스트 키 SSH 새 접속 검증 → 이전 관리 규칙 제거 → 대화형 SSH 접속 순서로 동작합니다. 서버를 시작하거나 NIC의 ACG 연결을 교체하지 않습니다.

동일 규칙은 추가하지 않습니다. 삭제는 로컬 관리 기록과 기기별 규칙 설명이 모두 일치하는 TCP 22 `/32`에만 허용됩니다. 기존 수동 규칙과 다른 기기의 규칙은 자동 편입·삭제하지 않습니다. 이번 도구 도입 전의 식별 표시 없는 규칙도 보존합니다. 관리 기록을 분실하면 남은 규칙을 자동 인수하지 않습니다.

API 삭제 요청이 서버에서 수락된 뒤 응답만 유실되는 경우에는 실제 삭제 여부가 불확실할 수 있습니다. 이 경우 추가 변경 없이 중단하고 다음 실행에서 재조회합니다. 이미 성공한 삭제까지 되돌리는 트랜잭션이나 무조건적인 rollback을 제공하지 않습니다.

IP·API·TCP·SSH·상태 저장 검증에 실패하면 중단합니다. 새 규칙을 추가한 뒤 실패한 경우 새 규칙은 남을 수 있지만 검증 전 이전 규칙은 삭제하지 않습니다. 의도를 추가 요청 전에 원자적으로 저장하므로 응답 유실 후 재실행하면 실제 규칙을 재조회해 중복 추가를 피합니다. OS 파일 잠금으로 동일 노트북의 동시 갱신을 막고 프로세스 종료 시 잠금은 해제됩니다. 다른 컴퓨터나 콘솔의 동시 변경까지 잠그지는 못합니다. 삭제 직전 소유 표시를 재확인하지만 API에 조건부 삭제 기능이 없어 외부 동시 수정과의 짧은 경쟁 가능성은 남습니다.

## 로컬 설치와 사용

기존 `%LOCALAPPDATA%\TradingAutomation\provisioning`의 상태·입력 JSON, developer 개인키와 검증된 known_hosts를 사용합니다. 원래 `connect-developer.ps1`은 같은 저장소 밖 폴더의 날짜별 `.bak`로 보존하며 원본 bytes 일치를 검사했습니다. 인증 설정·상태·입력 JSON은 변경하지 않습니다. 설치본은 독립 복사본이므로 저장소 코드를 수정한 뒤에는 다시 설치해야 합니다.

저장소 루트에서 재설치:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-connect-developer.ps1
```

이는 해당 자식 프로세스에만 적용되며 영구 실행 정책은 바꾸지 않습니다. 기본 인증 프로필은 `ssh-acg`입니다. 없는 경우 자동으로 다른 인증을 사용하지 않고 중단합니다.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$env:LOCALAPPDATA\TradingAutomation\provisioning\connect-developer.ps1" -DryRun
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$env:LOCALAPPDATA\TradingAutomation\provisioning\connect-developer.ps1"
```

2026-11-11에는 기존 `research-readonly`·`provisioning` 프로필의 dry-run과 명시적으로 선택한 `provisioning` 프로필의 실제 추가·TCP·SSH 검증을 수행했습니다. 기존 provisioning은 생성용 권한도 있으므로 전용 최소 권한 인증으로 대체할 대상이며 새 도구가 생성용 키의 상시 유지를 요구하지는 않습니다. 기존 인증으로 임시 접속할 때만 위 명령에 `-Profile provisioning`을 명시합니다. `-VerifyOnly`는 실제 갱신·새 SSH 검증까지 수행하고 대화형 터미널은 열지 않습니다. `-DryRun`은 클라우드·관리 기록을 바꾸지 않으며 중복 실행 방지용 로컬 잠금 파일만 사용합니다.

출력은 변경 여부·삭제 수·정적 오류만 포함합니다. 실제 IP·리소스 ID·API 응답·인증정보를 출력하거나 로그에 저장하지 않습니다. 대화형 접속 후 사용자가 실행하는 원격 명령의 출력은 별개입니다. API 키는 로컬 `~/.ncloud/configure`에서 읽기만 하며 서버로 전송·복사하지 않습니다. 신규 관리 기록과 잠금은 저장소 밖 `ssh-acg-managed.private.json`·`ssh-acg.lock`에 보관합니다.

## 전용 인증 준비

기존 인증이 없거나 거부되면 재시도하며 권한을 넓히지 않습니다. 사용자가 메인 콘솔에서 API Gateway 전용 Sub Account와 `ssh-acg` 로컬 프로필을 직접 준비합니다. 콘솔 로그인 권한·서버 생성/시작·ACG 생성/삭제·IAM 관리 권한은 이 도구에 필요하지 않습니다. 토큰·키를 채팅에 보내지 않습니다.

공식 [Server 권한 관리](https://guide.ncloud-docs.com/docs/server-subaccount-vpc)에 근거한 시작 권한 집합은 아래와 같습니다. 콘솔의 연관 액션 요구와 리소스별 제한을 확인해야 하며 새 전용 정책의 서비스 측 검증은 아직 하지 않았습니다.

| 용도 | 사용자 정의 정책 액션 |
| --- | --- |
| 서버 조회 | `View/getServerInstanceList`, `View/getServerInstanceDetail` |
| NIC 조회 | `View/getNetworkInterfaceList`, `View/getNetworkInterfaceDetail` |
| ACG 조회 | `View/getACGList`, `View/getACGDetail` |
| 규칙 추가·삭제 | `Change/setACGConfiguration` |

변경 권한은 콘솔이 지원하는 리소스 제한으로 지정 ACG에 한정합니다. 이 액션은 TCP 22 한 규칙에만 제한되는 IAM 권한이 아니며, 인바운드 SSH만 변경하도록 하는 추가 제한은 도구 코드에 있습니다. NIC 조회 문서의 연관 액션에는 더 넓은 기능도 섞여 있으므로 무조건 전체를 부여하지 말고 실제 거부 항목을 공식 문서·콘솔과 대조합니다. 부족하면 중단하고 필요한 항목을 별도 검토합니다.

API Gateway 접근 소스를 특정 IP로 제한한 계정은 핫스팟 변경 시 API 자체도 거부될 수 있습니다. 도구는 이 제한을 바꾸지 않습니다. 사용자가 콘솔에서 새 소스를 허용하거나 고정 출구망을 마련해야 합니다. [공식 Sub Account 접근 소스 안내](https://guide.ncloud-docs.com/docs/en/subaccount-use)를 참고하세요. SSH ACG를 전체 공개하는 방식으로 해결하지 않습니다.

API 형식의 근거: [NIC 목록](https://api.ncloud-docs.com/docs/compute-vserver-networkinterface-getnetworkinterfacelist), [규칙 추가](https://api.ncloud-docs.com/docs/compute-vserver-acg-addaccesscontrolgroupinboundrule), [규칙 삭제](https://api.ncloud-docs.com/docs/compute-vserver-acg-removeaccesscontrolgroupinboundrule). 삭제 요청은 규칙의 protocol·source·port 조합으로 지정하며 조건부 소유 검사 기능은 문서화돼 있지 않습니다.

## tmux 재접속

새 SSH 연결 후 기존 세션을 조회하고 이름을 지정합니다.

```bash
tmux ls
tmux attach -t <session-name>
```

새 세션이 필요하면 `tmux new -s work`를 사용합니다. 분리는 `Ctrl+b` 다음 `d`입니다. SSH 연결 자체를 복원하는 기능은 아니며 tmux 세션이 서버에 남아 있을 때 작업 화면으로 다시 접속합니다. 서버 재부팅 후 사라진 프로세스나 tmux 세션을 복구하지 않습니다.

## 개발 검증 명령

저장소 루트에서 실행합니다. Python 3.11.9, Ruff 0.14.4에서 아래 설치·테스트·lint·format 검사를 검증했습니다.

```powershell
python -m pip install --target .venv-tools -r requirements-dev.txt
python -m unittest discover -s tests -p "test_*.py" -v
.\.venv-tools\bin\ruff.exe check scripts tests
.\.venv-tools\bin\ruff.exe format --check scripts tests
```

테스트는 live 계정·네트워크 없이 규칙 소유권, 추가 후 실패, 중복 재실행, IP 변경, API 오류, 연결 실패, 잠금, 수동 편집 보존을 검증합니다. 실제 다른 네트워크 전환과 이전 관리 규칙 삭제는 mock 테스트 범위이며 실환경 전환 시험과 구분합니다.

최종 검토본은 Windows에서 26개 테스트를 통과했습니다. 다른 OS에서는 Windows 전용 잠금 테스트 1개를 명시적으로 skip하며 Linux에서의 전체 실행은 아직 확인하지 않았습니다. 동시 변경으로 다른 작업이 먼저 추가·삭제한 규칙은 실제 실행 결과 수량에 포함하지 않고 dry-run은 예정 수량을 표시합니다. 오류 안내도 이미 성공한 삭제가 자동 복원됐다고 보장하지 않습니다. 이 보완은 검토 worktree의 소스에만 반영됐으며 앞선 실환경 시험 설치본과는 구분합니다. 최신 검토본 사용 시 설치기를 다시 실행해야 합니다.
