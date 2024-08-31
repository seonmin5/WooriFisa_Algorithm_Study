"""
https://www.acmicpc.net/problem/2231
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().strip())

answer = 1000000

for i in range(n, 0, -1):
    a = [int(i) for i in str(i)]
    if i + sum(a) == n:
        if i <= answer:
            answer = i

print(str(answer) if answer != 1000000 else str(0))