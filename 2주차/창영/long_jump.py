def solution(n):
    answer = 0
    a, b = 0,1
    
    for i in range(n) :
        a,b = b, a+b
    
    answer = b % 1234567
    return answer
if __name__ == "__main__":
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))
    print(solution(5))