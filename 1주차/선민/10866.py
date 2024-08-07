from collections import deque
import sys
input = sys.stdin.readline

num = int(input())
deq = deque()

for _ in range(num):
    dequeCommand = input().split()
    if dequeCommand[0] == "push_front":
        deq.appendleft(dequeCommand[1])
    elif dequeCommand[0] == "push_back":
        deq.append(dequeCommand[1])
    elif dequeCommand[0] == "pop_front":
        if deq:
            print(deq.popleft())
        else:
            print("-1")
    elif dequeCommand[0] == "pop_back":
        if deq:
            print(deq.pop())
        else:
            print("-1")
    elif dequeCommand[0] == "size":
        print(len(deq))
    elif dequeCommand[0] == "empty":
        if deq:
            print(0)
        else:
            print(1)
    elif dequeCommand[0] == "front":
        if deq:
            print(deq[0])
        else:
            print("-1")
    elif dequeCommand[0] == "back":
        if deq:
            print(deq[-1])
        else:
            print("-1")
