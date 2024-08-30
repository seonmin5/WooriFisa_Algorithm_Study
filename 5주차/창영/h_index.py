def solution(citations):
    citations.sort(reverse=True)
    
    h_index = 0
    
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index


if __name__ == "__main__":
    print(solution([3, 0, 6, 1, 5])) # 3
    print(solution([1,10,11])) # 2
    print(solution([10,11])) # 2
    print(solution([0,0,0,0,0])) # 0
    
    """
    어떤 과학자가 발표한 논문 n편 중 h번 이상 인용된
    논문이 h번 이상이고, 나머지 논문이 h번 이하면
    h의 최대값이 이 과학자의 h-index임
    어떤 과학자가 발표한 논문의 인용 횟수인 
    citations가 매개변수로 주어짐 이 때 h-index 구하라
    
    """