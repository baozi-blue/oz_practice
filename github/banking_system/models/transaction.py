
class Transaction:
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance

    def __str__(self) -> str:   # 타입힌트로 메서드의 리턴 타입 지정 "->"
        return f"{self.transanction_type}: {self.amount}원, 잔고: {self.balance}원"
    
    def to_tuple(self) -> tuple:
        return self.transaction_type, self.amount, self.balance