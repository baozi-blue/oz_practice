# 아아: 5000원  / 아샷추: 6500원
# 아아 2잔 / 아샷추 3잔
# 변수 사용하지 않을때 이전에 계산된 결과 저장 불가
(5000*2) + (6500*3)


# 변수 사용
a = 5000
b = 6500
c = a*2 + b*3
print(c)


num_1, num_2 = 1, 2
print(num_1)
print(num_1, num_2)

# 변수에 값을 넣는 것 -> '할당(assignment)'
# 복합 연산자: '+=' 산술 후 바로 할당하는 문법 -> 생산성 UP
sum = 1 + 2
sum = sum + 3
print(sum)

sum2 = 1 + 2
sum2 += 3
print(sum2)

# 변수명 규칙 주의
snake_case = 1
snake__case = 2
camelCase = 3


# 포메팅 f-string
guest_name = "Emma"
print(f'{guest_name}만 빼고 고양이 다 있어')

# 붕어빵 과제
# 변수값 입력
fishcake__bean, fishcake__shucream, fishcake__jabchae = "붕어빵(팥)", "붕어빵(슈크림)", "붕어빵(잡채)"
fishcake__bean_p, fishcake__shucream_p, fishcake__jabchae_p = 2000, 2500, 3000
order_1, order_2 = 3, 2

# 총 결제금액
total_price = fishcake__jabchae_p*order_1 + fishcake__shucream_p*order_2

# 출력
print(f'주문이 완료되었습니다.{fishcake__jabchae} {order_1}개, {fishcake__shucream}{order_2}개, 총 결제 금액은{total_price}원입니다.')



