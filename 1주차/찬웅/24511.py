from collections import deque

n = int(input()) # 자료구조의 개수
A = list(map(int, input().split())) # 큐면 0, 스택 1 
B = list(map(int, input().split())) # 원소
M = int(input()) # 수열의 길이
C = list(map(int, input().split())) # questack에 삽입합 원소를 담고 있는 수열

deq = deque()
for i in range(n):
    if A[i] == 0: 
        deq.append(B[i])

for j in range(M): 
    deq.appendleft(C[j])  

for _ in range(M):
    print(deq.pop(), end=" ")