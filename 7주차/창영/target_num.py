def solution(numbers, target):
    def dfs(index, current_sum):
        # 모든 숫자를 사용한 경우
        if index == len(numbers):
            # 현재 계산된 값이 타겟 넘버와 같은지 확인
            if current_sum == target:
                return 1
            else:
                return 0
        # 현재 숫자를 더하거나 빼는 두 가지 경우의 수를 탐색
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
    
    # DFS 시작, 처음에는 인덱스 0과 합계 0에서 시작
    return dfs(0, 0)


if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))