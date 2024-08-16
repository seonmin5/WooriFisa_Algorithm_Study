def solution(answers):
    answer = []
    
    person1 = [1, 2, 3, 4, 5] * (len(answers) - 1)
    person2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) - 1)
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) - 1)

    person_count = [0 for _ in range(3)]
    
    for i in range(len(answers)):
        if person1[i] == answers[i]:
            person_count[0] += 1
        
        if person2[i] == answers[i]:
            person_count[1] += 1
            
        if person3[i] == answers[i]:
            person_count[2] += 1
            
    if person_count[0] >= person_count[1] and person_count[0] >= person_count[2]:
        answer.append(1)
    
    if person_count[1] >= person_count[0] and person_count[1] >= person_count[2]:
        answer.append(2)

    if person_count[2] >= person_count[0] and person_count[2] >= person_count[1]:
        answer.append(3)
        
    return answer

if __name__ == "__main__":
    print(solution(	[1, 3, 2, 4, 2]))