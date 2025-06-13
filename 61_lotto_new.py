def solution(lottos, win_nums):
    answer = []
    count_correct = 0
    count0 = 0
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    for i in lottos:
        if i in win_nums:
            count_correct += 1
        elif i == 0:
            count0 += 1
    answer = [rank[count_correct + count0], rank[count_correct]]
    
    return answer
    
    
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))