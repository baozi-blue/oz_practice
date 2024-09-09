
# tuple 및 list의 차이점 :
# 1) 리스트 [] / 튜플 ()
# 2) 리스트는 요솟값의 생성/삭제/수정이 가능화지만 튜플은 요솟값을 바꿀 수 없다. 
# i.e. 변경하면 안되는 값들 저장 시 튜플 사용


# 다양한 tuple의 선언 방식
t1 = ()
t2 = (1, )
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

print(type(t5))
# <class 'tuple'>

print(dir(t5))
# tuple 내 사용 가능한 내장함수 :
# '__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', 
# '__sizeof__', '__str__', '__subclasshook__', 'count', 'index'
# sort / insert / remove / pop 등 내장함수 사용불가

# tuple => list 변환
t6 = list(t5)
print(t6)
print(type(t6))

# tuple 곱하기 (반복)
t7 = t3 * 2
print(t7)



a = "abcde"
b = list(a)
c = tuple(a)
print(b)
print(c)

e = "".join(b)
print(e)

f = "".join(c)
print(f)

c[2]
c.index('a')
c.count('a')
len(c)


# list는 tuple보다 무겁다. 추가 할당 시 메모리 크기는 더블링 진행하기 때문.
# python는 c언어로 만들어졌고 동적배열을 지원한다.


