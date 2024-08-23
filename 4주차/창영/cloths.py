from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(list)
    
    for name, kind in clothes:
        clothes_dict[kind].append(name)

    combinations = 1
    for kind in clothes_dict:
        combinations *= (len(clothes_dict[kind]) + 1)

    return combinations - 1

# 예제 테스트
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) # 출력: 5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) # 출력: 3
