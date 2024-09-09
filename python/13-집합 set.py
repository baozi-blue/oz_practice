
# set은 수학의 집합을 의미함.
# 순서 X, 값 중복 X

# set 생성 : s = {} / s = set()
s1 = set([1, 2, 3, 'a', 'b'])
print(type(s1))
print(s1)

s2 = set('blablabla')
s2
# >>> {'b', 'l', 'a'}
# 값 중복 허락하지 않고 출력 순서 매번 다를 수 있음


# set 자료형의 데이터 추가, 삭제, 변경
s1.add('tomato')
s1

s1.update('apple')
s1
# >>> {1, 2, 3, 'tomato', 'e', 'l', 'a', 'b', 'p'}

s1.remove('tomato')
s1

re = {'a', 'p', 'l', 'e'}
s1.remove(re)
# >>> Keyerror

s1.remove('a')
s1.remove('p')
s1.remove('l')
s1.remove('e')

s1.discard('b')
s1.discard(1)

s1

# .pop() 반환 : 첫번째 값 삭제됨
s1.pop()
s1





# 집합, 합집합, 교집합, 차집합 etc..
s3 = {'당근','양파','오이','배추'}
s4 = {'양파','오이','대파','가지'}

set.union(s3, s4)
set.intersection(s3, s4)
set.difference(s3, s4)
# >>> {'배추', '당근'} => '가지'는 ???








print(' * ', ' * ', ' * ', ' * ', ' * ', ' * ', sep='x')
x, y = map(float, input('실수를 입력하세요: ').split())