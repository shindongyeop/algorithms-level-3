def solution(numbers):
    answer = []
    n_length = len(numbers)
    for i in range(n_length):
        print(f'i: {i}')
        for j in range(i + 1, n_length):
            print(f'i + 1: {i + 1}, j: {j}')
            print(f'numbers[i]: {numbers[i]}, numbers[j]: {numbers[j]}')    
            S = numbers[i] + numbers[j]
            print(f'numbers[i] + numbers[j] = {S}')
            answer.append(S)
            print(f'answer.append({S}): {answer}')
    
    answer = sorted(set(answer))
    
    return answer

print(solution([2,1,3,4,1]))