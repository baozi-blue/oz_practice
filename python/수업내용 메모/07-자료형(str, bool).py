# str : 문자열
# 특징 : 시퀸스 자료형 - 요소들이 연속적으로 이어진 자료형

a = "순서대로 문자를 추출하겠습니다"

# 요소 합치기
b = a[0] + a[2] + a[4]
print(b)

# 요소의 복사
print(a*2)

# 요소 슬라이싱
a[5]
a[7]
a[-2]

# 5 <= x < 7
print(a[5:7])
print(a[5:-9])

date = "2000.12.25"
yy = date[0:4]
mm = date[5:7]
dd = date[8:10]

print(f'{yy}년{mm}월{dd}일')

# count : 요소 개수 합산
date.count("0")

# index : 몇번째 요소인지 확인
date.index("5")

# len : 문자열 길이 확인
len(date)

# find: 위치 알려주기
date.find('5')







