# 내장함수: https://docs.python.org/ko/3/library/functions.html
input() 
print()

greeting = input()
print(greeting + "신기해")


# int(), float(), str(), bool()

정수 = input()
정수 = int(정수)
# 정수 = int(input())

print(정수, type(정수))


num1, num2, num3, num4 = map(int.input().split(","))
print(type(num1), num2, num3, num4)


# tuple(), list(), dict(), set(), map(), split()

def add(x, y):
    return x + y

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]
added_numbers = map(add, numbers1, numbers2)
print(list(added_numbers))


