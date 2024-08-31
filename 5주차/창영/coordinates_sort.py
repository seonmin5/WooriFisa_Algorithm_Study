'''
5
3 4
1 1
1 -1
2 2
3 3
'''

import sys
input = sys.stdin.readline
print = sys.stdout.write

x = []
y = []

for _ in range(int(input().strip())):
    a, b = map(int, input().strip().split())
    x.append(a)
    y.append(b)

for i, k in sorted(zip(x, y)):
    print(str(i) + ' ' + str(k) + '\n')
