import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

stack = []
order = 1
for number in numbers:
    while stack and stack[-1] == order:
        stack.pop()
        order += 1
    
    if number == order:
        order += 1
    else:
        stack.append(number)

while stack and stack[-1] == order:
    stack.pop()
    order += 1

if order == n + 1:
    print("Nice")
else:
    print("Sad")