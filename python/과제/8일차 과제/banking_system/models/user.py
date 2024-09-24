# User 클래스 구현
# username과 account를 초기화하는 생성자를 구현합니다.

# 변수 컨벤션:
# username: 사용자의 이름을 나타내는 문자열
# account: 사용자의 계좌를 나타내는 Account 객체


from banking_system.models.account import Account

class User:
    def __init__(self, username: str) -> None:
        self.username = username
        self.account = Account()