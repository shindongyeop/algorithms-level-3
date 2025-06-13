def solution(number, limit, power):
    divisors = [0] * (number + 1)
    iron = 0
    # Calculate the number of divisors
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors[j] += 1
            print(f'divisors[{j}] = {divisors[j]}')
      
    for i in range(1, number + 1): 
        if divisors[i] > limit:
            iron += power
        else:
            iron += divisors[i]
            
    return iron

print(solution(5, 3, 2)) # output 10
print(solution(10, 3, 2))  # output 21