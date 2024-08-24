import sys
input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    a = int(input())
    numbers.append(a)

numbers.sort()

for i in numbers:
    print(i)