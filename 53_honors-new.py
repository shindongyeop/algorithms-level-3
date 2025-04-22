def solution(k, score):
    hall_of_fame = []
    result = []
    for day, sc in enumerate(score):
        hall_of_fame.append(sc)
        hall_of_fame.sort(reverse=True)
        if len(hall_of_fame) > k:
            hall_of_fame.pop()
        result.append(hall_of_fame[-1])
    return result