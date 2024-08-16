import sys
input = sys.stdin.readline
s = input() # baekjoon
alpha = ["-1" for _ in range(26)]

for i in range(97, 97 + 26):
    if chr(i) in s:
        alpha[i - 97] = str(s.index(chr(i)))

print(" ".join(alpha))
