import sys
input = sys.stdin.readline

from itertools import product

n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]

for num in product(numbers, repeat=m):
    
    if list(num) == sorted(num): # 비내림차순인지 check
        print(*num)