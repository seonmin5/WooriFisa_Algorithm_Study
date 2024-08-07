def solution(arr): # gcd와 lcm 코드 구현방법 외우기
    answer = 1
    for i in arr:
        answer = lcm(answer, i)

    return answer

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

def lcm(n, m):  
    return n // gcd(n, m) * m

if __name__ == "__main__":
    print(solution([2,6,8,14]))
    print(solution([1,2,3]))