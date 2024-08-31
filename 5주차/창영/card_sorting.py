"""
정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다.

이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.

매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다.

예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다.

그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.

N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.

첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다.

숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.

입력        
3
10
20
40

출력
100
"""
# gpt 풀이: heapq를 이용하여 훨씬 빠르고 정확한 풀이를 구현하였다. heapq를 자세히 알아봐야겠다.
import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

total_comparisons = 0

while len(heap) > 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    
    combined = first + second
    
    heapq.heappush(heap, combined)
    
    total_comparisons += combined

print(str(total_comparisons))

# 내 풀이: 정답은 나오지만 계산속도가 느려 효율적인 결과가 나오지 않음
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write
# from collections import deque

# arr = deque()
# a = []
# for _ in range(int(input())):
#     a.append(int(input()))
    
# a.sort()
# arr.extend(a)
# answer = 0
# temp = []
# while True:
#     while arr:
#         if len(arr) >= 2:
#             a1 = arr.popleft()
#             a2 = arr.popleft()
#             arr.appendleft(a1 + a2)
#             temp.append(a1 + a2)
#         else:
#             break
        
#     if len(temp) == 1:
#         break
    
#     arr.clear()
#     arr.extend(temp)
#     temp.clear()
    
# print(temp[0])