import sys
input = sys.stdin.readline

n = int(input())
nList = []

for _ in range(n):
    i = int(input())
    nList.append(i)

nList.sort()

for i in nList:
    print(i)