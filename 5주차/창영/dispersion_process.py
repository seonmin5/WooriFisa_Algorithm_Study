import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    
    temp = []

    for i in range(1, int(b) + 1):
        if temp == []:
            temp.append(str(int(a) ** i))
        else:
            if str(int(a) ** i)[-1] in temp:
                break
            else:
                temp.append(str(int(a) ** i)[-1])

    print(temp[((int(b) - 1)% len(temp))])