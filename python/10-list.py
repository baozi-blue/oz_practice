# 리스트 생성
a = [1, 3, 5]
b = [2, 4, 6]


# 리스트 합치기
c = a + b
print(c)

# list 포함된 list
d = [1, 2, 3 , ['a', 'b', 'c']]
d[0]
d[-1]
d[3]
d[3][0]
d[0:2]


# list(range(시작, 끝, 간격))
a = range(0, 20, 4)
print(a)

b = list(a)
print(b)

c = list(range(0, 20, 4))
print(c)

# 리스트 패킹, 언패킹
# split 은 따로 지정 안할 때 "빈칸" 기준으로 나눈다
input().split()
# 안 녕 -> 입력
# 결과 -> ['안', '녕']


# list 값 추가/변경/삭제
# 값 추가
food = ['pizza','burger','spaghetti','french fries']
food.append('soup')
print(food)

# 지정 위치에 값 추가하기
food.insert(1, 'salad')
print(food)

# 값 삭제하기
del food[-1]
print(food)

# 값 바꾸기
food[-1] = 'soup'
print(food)


print(dir(list))
# 내장 메소드
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']  ---> 지즈 쓰는 메소드


food.reverse()
print (food)

food.sort()
print (food)






















