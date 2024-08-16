from itertools import permutations
def solution(numbers):
    answer = 0
    distinct_set = set()
    for i in range(len(numbers) + 1):
        for j in permutations(numbers, i):
            
            if [k for k in j] != []:
                distinct_set.add(int(''.join([k for k in j])))

    for i in distinct_set:
        is_prime = True
        
        if i == 0 or i == 1:
            is_prime = False
            
        else:
            for j in range(2, int(i ** 0.5) + 2):
                if i != 2 and i % j == 0:
                    is_prime = False
                    break
        if is_prime:
            answer += 1
            
    return answer

if __name__ =="__main__":
    # print(solution("17"))
    # print(solution("011"))
    print(solution("121"))