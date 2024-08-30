import sys
input = sys.stdin.readline

<<<<<<< HEAD
# 총 데이터 개수: a**b개 -> 이걸 다 계산하면 시간초과 뜸
# 마지막 데이터가 처리될 컴퓨터 번호는?
# a**b의 %10 => 나머지

t = int(input().strip())  # 테스트 케이스 개수

for _ in range(t):
    a, b = map(int, input().strip().split())
    
    a = a % 10  # a의 마지막 자리만 보면 돼
    
    if a == 0:
        print(10)  # a의 마지막 자리가 0이면 결과는 10번 컴퓨터
        continue
    
    # 패턴 만들기
    pattern = []
    temp = a
    while temp not in pattern:
        pattern.append(temp)
        temp = (temp * a) % 10
    
    # 패턴에서 b번째 자리 찾기
    index = (b - 1) % len(pattern)
    print(pattern[index])
=======
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
>>>>>>> daac2b5960c78b482c33aa3ce4e7a3db33a1bd07
