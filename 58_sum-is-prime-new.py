def is_prime(n):
    """ Check if a number is prime. """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if is_prime(nums[i] + nums[j] + nums[k]) == True:
                    answer += 1 
    
    return answer


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))