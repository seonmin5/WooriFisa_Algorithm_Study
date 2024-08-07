from itertools import combinations
import time
def solution(elements):
    answer = 0
    res = set()
    for i in range(1, len(elements) + 1):
        for j in set(combinations(elements, i)):
            if len(j) == 1:
                res.add(j[0])
            elif abs(elements.index(j[0]) -  elements.index(j[1])) <= 1:
                res.add(sum(j))
                
        print(res)
        time.sleep(10)
        
    print(len(res))
    return answer

if __name__ == "__main__":
    print(solution([7,9,1,1,4]))