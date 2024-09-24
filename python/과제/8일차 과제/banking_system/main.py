# 메인 함수 구현

#1. BankingService 인스턴스를 생성합니다.
#2. 사용자로부터 입력을 받아 사용자 추가 및 찾기 기능을 제공합니다.
#3. 사용자 메뉴를 통해 입금, 출금, 잔고 확인, 거래 내역 기능을 실행할 수 있도록 합니다.

# 프로그램의 시작점으로 이해해야 함
# VSC 디버깅 기능 활용, 코딩 유치원


import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.banking_service import BankingService      # 수정: 상위 폴더명 삭제
from utils.exceptions import InsufficientFundsError, NegativeAmountError, UserNotFoundError
from models.account import Account
from models.user import User

if __name__ == "__main__":
    banking_service = BankingService()

    while True:
        print("1. 사용자 추가")
        print("2. 사용자 찾기")
        print("3. 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            username = input("사용자 이름을 입력하세요: ")
            account = Account(0, [])     # 위에 import 추가
            user = User(username, account)
            banking_service.add_user(user)
            print(f"{username} 사용자 추가 완료")

        elif choice == '2':
            username = input("찾을 사용자 이름을 입력하세요: ")
            user = banking_service.find_user(username)
            if user:
                print(f"{username} 사용자 찾기 완료")
                banking_service.user_menu()
            else:
                print("사용자를 찾을 수 없습니다.")

        elif choice == '3':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 메뉴를 선택했습니다.")
