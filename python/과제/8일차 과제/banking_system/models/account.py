# Account 클래스 구현

#1. __balance와 transactions 리스트를 초기화하는 생성자를 구현합니다.
#2. 입금을 위한 deposit 메서드를 구현합니다.
#3. 출금을 위한 withdraw 메서드를 구현합니다.
#4. 잔고를 반환하는 get_balance 메서드를 구현합니다.
#5. 거래 내역을 반환하는 get_transactions 메서드를 구현합니다.
#6. 클래스 변수 bank_name와 클래스 메소드 get_bank_name, set_bank_name을 구현합니다.

# 변수 컨벤션:

#- __balance: 계좌 잔고를 나타내는 프라이빗 정수 변수
#- transactions: 거래 내역을 저장하는 리스트
#- bank_name: 은행 이름을 나타내는 클래스 변수 문자열
#- amount: 입금 또는 출금 금액을 나타내는 정수

class Account:
    
    __balance = []
    trasactions = []
    bank_name = "신한은행" 

    def __init__(self, __balance, transactions):
        self.__balance = __balance
        self.transactions = transactions
    
    def deposit(self, amount):
        self.__balance += amount
        self.transactions.append(Transaction("deposit", amount, self.__balance))
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.transactions.append(Transaction("withdraw", amount, self.__balance))
        else:
            print("잔액이 부족합니다.")
    
    def get_balance(self):
        return self.__balance
    
    def get_transactions(self):
        return self.transactions
    
    @classmethod
    def get_bank_name(cls): 
        return cls.bank_name
    
    @classmethod
    def set_bank_name(cls, bank_name): 
        cls.bank_name = bank_name
