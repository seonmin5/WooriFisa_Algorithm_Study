def solution(want, number, discount):
    answer = 0
    want_zip = {i: k for i, k in zip(want, number)}
    idx = 0
    while True:
        temp = discount[idx : idx + 10]
        temp_want_zip = want_zip.copy()
        if len(temp) < 10:
            break
        
        for i in temp:
            if temp_want_zip.get(i) != None and temp_want_zip.get(i) != 0:
                temp_want_zip[i] -= 1
                
        if sum(temp_want_zip.values()) == 0:
            answer += 1
        idx += 1
            
    return answer

if __name__ =="__main__":
    print(solution(
        ["banana", "apple", "rice", "pork", "pot"],
        [3, 2, 2, 2, 1],
        ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
        ))
    print(solution(
        ["apple"],
        [10],
        ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
        ))