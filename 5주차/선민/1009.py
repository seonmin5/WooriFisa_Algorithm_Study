import sys
input = sys.stdin.readline

# 테스트 케이스의 수
t = int(input().strip())

# 테스트 케이스에 대해 정수 a, b
for _ in range(t):
    a, b = map(int, input().strip().split())

    a %= 10

    if a == 0:
        print(10)
    else:
        # a의 마지막 자리가 반복되는 패턴 파악
        pattern = []
        temp = a
        while temp not in pattern:
            pattern.append(temp)
            temp = (a * temp) % 10 # a를 제곱 -> 마지막 자리 패턴 파악

        index = (b-1) % len(pattern)
        print(pattern[index])
