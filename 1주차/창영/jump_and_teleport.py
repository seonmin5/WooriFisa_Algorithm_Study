def solution(n):
    ans = 0
    distence = 0
    now = 0
    
    while n > now :
        if distence < 1 or distence > n:
            ans += 1
            distence += 1
            now += 1
        else:
            now += n // (distence * 2)
            distence *= 2
            
    return ans

if __name__ == "__main__":
    print(solution(5000))