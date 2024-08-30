import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    if n-i == 0:
        print(i*"*" + i*"*")
    else:
        print(i*"*" + (n-i)*" " + (n-i)*" " + i*"*")

for j in range(n-1, 0, -1):
    if n-j == 0:
        print(j*"*" + j*"*")
    else:
        print(j*"*" + (n-j)*" " + (n-j)*" " + j*"*")