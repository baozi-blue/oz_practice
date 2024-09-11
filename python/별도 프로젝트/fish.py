# terminal에서 새로운 파일 생성 : touch fish.py

# 재고 데이터 생성
stock = {"팥붕어빵" : 10, "슈크림붕어빵" : 8, "초코붕어빵" : 5}


order = {}
bread_type = input("주문할 제품명을 입력하세요.")
bread_count = int(input("주문할 개수를 입력하세요"))

order[bread_type] = bread_count
print(f'주문내역: {order}')

# 함수 - len(stock);  메소드 - stock.items()
for bread, quantity in stock.items():
    print(f'{bread} : {quantity}')