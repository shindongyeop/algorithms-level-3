def solution(array, commands):
    array_part = []
    answer = []
    ans = 0
    for i, j, k in commands:
        print(f'i, j, k = {i}, {j}, {k}')
        array_part = sorted(array[i - 1: j])
        print(f'array_part = {array_part}')
        array_part[k - 1]
        answer.append(array_part[k - 1])
        print(f'answer = {answer}')
    return answer
    
    
    
print(solution([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]])) # Output [5,6,3]