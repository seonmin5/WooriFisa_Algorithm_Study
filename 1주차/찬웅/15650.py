from itertools import combinations

n, m = map(int, input().split())

numbers = [i for i in range(1, n+1)]

for j in combinations(numbers, m):
    print(' '.join(map(str, j)))
    

