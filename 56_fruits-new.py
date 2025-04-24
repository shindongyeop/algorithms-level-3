def solution(k, m, score):
    result = 0
    S = sorted(score, reverse = True)
    # print(f'sorted score = {S}')
    for i in range(len(score) // m):
        # print(f'box number = {len(score) // m}')
        interest_each_box = S[(i + 1) * m - 1] * m
        # print(f'when i = {i}, (i+1)*m-1 = {(i + 1) * m - 1}, S = {S[(i+1) * m - 1]}, interest each box = {S[(i + 1) * (m -1)] * m}')
        result += interest_each_box
        # print(f'total interest = {result}')
    return result
  
  
print(solution(3, 4, [1,2,3,1,2,3,1]))
print(solution(4, 3, [4,1,2,2,4,4,4,4,1,2,4,2]))
    