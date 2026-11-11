# 테스트

`test_ssh_acg.py`는 Python 표준 `unittest`로 Windows 노트북의 SSH ACG 도구를 검사합니다. 실계정·네트워크 없이 소유권 판별, 추가 후 실패·재실행, 중복 방지, IP 변경, 기존 규칙 보존과 OS 잠금을 검증합니다. 분석·주문 앱 테스트는 아직 없습니다.

저장소 루트에서 `python -m unittest discover -s tests -p "test_*.py" -v`를 실행합니다. Python 3.11.9·Windows에서 검증했으며 실행 환경과 lint·format 명령은 [루트 README](../README.md)에 있습니다.

최종 검토에서는 26개 테스트가 통과했습니다. Windows 전용 OS 잠금 테스트는 다른 OS에서 skip하며 서버 Linux에서의 실행은 미검증입니다.
