
# 딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다. 
# 이것이 바로 딕셔너리의 가장 큰 특징이다. -> 데이터의 연관성
# dic = {Key1: Value1, Key2: Value2, Key3: Value3, ...}
# value 중복은 가능하나 key 중복 불가, key에 list를 넣을 수 없으나 tuple는 가능. -> key가 mutable/immutable 값인지에 달려 있다.
# list[], tuple(), dict{}

dic1 = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

# dict() : 딕셔너리 생성 함수
dic2 = dict(a=30, b=20, c=70, d=90)
print(dic2)

# zip() : 병렬 처리
dic3 = dict(zip(['a', 'b', 'c'],[20, 30, 50]))
print(dic3)


a = {1: 'a'}


# 값 추가
a[2] = 'b'
a[3] = 'c'
a['name'] = 'Emma'
a[4] = [1, 2, 3]
print(a)
# >>> {1: 'a', 2: 'b', 3: 'c', 'name': 'Emma', 4: [1, 2, 3]}

a.update({'5': 18, '6': 29})
print(a)
# >>> {1: 'a', 2: 'b', 3: 'c', 'name': 'Emma', 4: [1, 2, 3], '5': 18, '6': 29}

# 값 호출
a.get(2)

# 값 존재 여부확인
2 in a
'2' in a

# 값 변경
a['5'] = 'j'
print(a)
# >>> {1: 'a', 2: 'b', 3: 'c', 'name': 'Emma', 4: [1, 2, 3], '5': j, '6': 29}


# 값 삭제
del a[1]
print(a)
# >>> {2: 'b', 3: 'c', 'name': 'Emma', 4: [1, 2, 3], '5': 'j', '6': 29}



print(a.keys())
# >>> dict_keys([2, 3, 'name', 4, '5', '6'])

print(a.values())
# >>> dict_values(['b', 'c', 'Emma', [1, 2, 3], 'j', 29])

print(a.items())
a2 = list(a.items())
print(a2)
print(type(a2))




# 값을 모두 지우기
a.clear()
print(a)
# >>> {}





# 해시, 해시맵, 해시테이블 (?)



# 주문 데이터 연습
price = {'팥': 2000, '슈크림': 2500, '잡채': 3000}
order1 = map(int, input(f'맛 순서대로 구매 수량을 입력하세요(팥, 슈크림, 잡채)').split(','))
order2 = list(order1)

total_order = sum(order2)
total_amount = 0

total_amount += price['팥'] * order2[0]
total_amount += price['슈크림'] * order2[1]
total_amount += price['잡채'] * order2[2]

print(f'주문 완료되었습니다. 팥 {order2[0]}개, 슈크림 {order2[1]}개, 잡채 {order2[2]}개, 총 {total_order}개 주문했습니다. 결제금액은 {total_amount}원입니다.')






