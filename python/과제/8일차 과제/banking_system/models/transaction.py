# Transaction 클래스 구현

#1. 거래(Transaction) 클래스를 정의하고, transaction_type, amount, balance 속성을 초기화하는 생성자를 구현합니다.
#2. 거래 정보를 문자열로 반환하는 __str__ 메서드를 구현합니다.
#3. 거래 정보를 튜플로 반환하는 to_tuple 메서드를 구현합니다.

# 변수 컨벤션:

#- transaction_type: 거래 유형을 나타내는 문자열 (예: "입금", "출금")
#- amount: 거래 금액을 나타내는 정수
#- balance: 거래 후 잔고를 나타내는 정수


class Transaction:

    def __init__(self, transaction_type, amount, balance):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance

    def __str__(self):
        return f"{self.transaction_type} {self.amount} {self.balance}"
    
    def to_tuple(self):
        return
    


