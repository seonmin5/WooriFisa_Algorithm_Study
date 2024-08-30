import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    arr.append(input().strip().split())

for i in sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])):
    print(i[0])
