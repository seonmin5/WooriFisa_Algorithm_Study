def solution(elements):
    n = len(elements)
    extended_elements = elements * 2
    
    sum_set = set()
    
    for length in range(1, n+1):
        for start in range(n):
            subarray_sum = sum(extended_elements[start:start+length])
            sum_set.add(subarray_sum)
    
    return len(sum_set)

if __name__ == "__main__":
    print(solution([7,9,1,1,4]))