def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3,reverse=True)

    for i in numbers:
        answer += i

    return str(int(answer))

if __name__ == "__main__":
    print(solution([3, 30, 34, 5, 9]))