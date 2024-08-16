def solution(priorities, location):
    loc = []

    for _ in range(len(priorities)):

        for i in range(len(priorities)):
            if max(priorities) == priorities[i]:
                loc.append(i)
                priorities[i] = 0

            if len(loc) == len(priorities):        
                break

        if len(loc) == len(priorities):            
                break    
            
    return loc.index(location) + 1


if __name__ == "__main__":
    # print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))