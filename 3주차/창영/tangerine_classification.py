from collections import Counter
def solution(k, tangerine):
    answer = 1
    tangerine_count = dict(Counter(tangerine))
    classificationed_tangerine = sorted([i for i in tangerine_count.values()], reverse=True)
    for i in classificationed_tangerine:
        if k - i > 0:
            k -= i
            answer += 1
        else:
            break
        
    return answer

if __name__ == "__main__":
    print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) # result: 3
    print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])) # result: 2
    print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3])) # result: 1