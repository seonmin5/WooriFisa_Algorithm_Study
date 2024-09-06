import sys
input = sys.stdin.readline
print = sys.stdout.write

def binary_search(target,lis):
    start,end = 0,len(lis)-1
    while start < end:
        mid = (start + end) // 2 
        if lis[mid] == target:
            return mid
        elif lis[mid-1] < target < lis[mid]: 
            return mid
        elif target < lis[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start 

def sol():
    n = int(input())
    a = list(map(int,input().split()))
    lis = [a[0]] 
    for i in range(1,n):
        target = a[i]
        if lis[-1] < target: 
            lis.append(target)
        else:
            idx = binary_search(target,lis)
            lis[idx] = target

    return len(lis) 

print(str(sol()))