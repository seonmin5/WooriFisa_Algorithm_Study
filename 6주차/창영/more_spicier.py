import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        if scoville[0] >= K:
            break
        least_spicy = heapq.heappop(scoville)
        if not scoville:
            break
        new_spicy_food = least_spicy + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_spicy_food)
        answer += 1
    return answer if scoville else -1 

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12]	, 7))