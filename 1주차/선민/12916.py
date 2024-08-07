def solution(s):
    countP = 0
    countY = 0
    lowerS = s.lower()
    for i in lowerS:
        if i == "p":
            countP += 1
        elif i == "y":
            countY += 1
    if countP == countY:
        return True
    else:
        return False