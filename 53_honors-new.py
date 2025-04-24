def solution(k, score):
    result = []
    hall_of_fame = []
    for day, sc in enumerate(score):
        hall_of_fame.append(sc)
        # print(f'appended hall_of_fame = {hall_of_fame}')
        hall_of_fame.sort(reverse=True)
        # print(f'sorted hall_of_fame = {hall_of_fame}')
        if len(hall_of_fame) > k:
            hall_of_fame.pop()
            # print(f'trimmed hall_of_fame = {hall_of_fame}')
        result.append(hall_of_fame[-1])
        # print(f'lowest score = {result}')
    return result 

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))