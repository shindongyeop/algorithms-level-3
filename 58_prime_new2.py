def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                count += 1

def solution(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_prime(nums[i] + nums[j] + nums[k]) == True:
                    count += 1
    return count


print(solution([1,2,3,4])) # output 1
print(solution([1,2,7,6,4]))  # output 4


    