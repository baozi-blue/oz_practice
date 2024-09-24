# BankingService 클래스 구현

#1. 사용자 목록을 초기화하는 생성자를 구현합니다.
#2. 사용자를 추가하는 add_user 메서드를 구현합니다.
#3. 사용자를 찾는 find_user 메서드를 구현합니다.
#4. 사용자 메뉴를 제공하는 user_menu 메서드를 구현합니다.

# 변수 컨벤션:

#- users: 사용자 목록을 저장하는 리스트
#- username: 사용자의 이름을 나타내는 문자열
#- user: User 객체를 나타내는 변수
#- amount: 입금 또는 출금 금액을 나타내는 정수
#- choice: 사용자의 선택을 나타내는 문자열


from models.user import User
from utils.exceptions import UserNotFoundError

class BankingService:
    def __init__(self) -> None:
        self.users = []

    def add_user(self, username: str) -> None:
        self.users.append(User(username))

    def find_user(self, username: str) -> None:
        for user in self.users:
            if user.username == username:
                return user
        raise UserNotFoundError(username)

    def user_menu(self, username: str) -> None:
        user = self.find_user(username)

        print("사용자 메뉴")
        print("1. 입금")
        print("2. 출금")
        print("3. 잔액 확인")
        print("4. 거래 내역 확인")
        print("5. 종료")

        while True:
            choice = input("메뉴를 선택하세요: ")
            if choice == '1':
                amount = int(input("입금할 금액을 입력하세요: "))
                user.account.deposit(amount)
            elif choice == '2':
                amount = int(input("출금할 금액을 입력하세요: "))
                user.account.withdraw(amount)
            elif choice == '3':
                print(f'현재 잔액은: {user.account.get_balance()}원 입니다.')
            elif choice == '4':
                print(user.account.get_transactions())
            elif choice == '5':
                print("서비스 종료합니다.")
                break
            else:
                print("잘못된 메뉴를 선택했습니다.")