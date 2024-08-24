from collections import deque
import sys
input = sys.stdin.readline

# strip(): 줄바꿈 문자 제거용
n = int(input().strip())
stack = deque()

# push, pop, size, empty, top
# push: 정수 x 받아야 함
# pop: 스택에 정수가 없다면 -1 출력
# empty: 비어 있으면 1, 아니면 0 출력
# top: 스택에 정수가 없다면 -1 출력
for _ in range(n):
    command = input().strip().split()

    if command[0] == "push":
        stack.append(command[1])
    
    elif command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif command[0] == "size":
        print(len(stack))
    
    elif command[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    
    elif command[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
        
        
