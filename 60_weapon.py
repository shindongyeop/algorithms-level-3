def solution(number, limit, power):
    # Initialize an array to hold divisor counts for each number
    divisors = [0] * (number + 1)
    
    # Efficiently calculate the divisor counts using sieve method
    for i in range(1, number + 1):
        for j in range(i, number + 1, i): 
            print(f'i = {i} and j = {j}')
            divisors[j] += 1
            print(f'divisors[{j}] = {divisors[j]}')
        
        #. Calculate the total amount of iron needed
    iron = 0
    for i in range(1, number + 1):
        if divisors[i] > limit:
            iron += power # Use 'power' if divosor coucount exceeds limit
        else:
            iron += divisors[i] # Otherwise, use actual divisor count
                
    return iron      
    
print(solution(5, 3, 2))  #Output 10
