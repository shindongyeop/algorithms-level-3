def solution(n, m, section):
    painted = 0
    count = 0
    for sec in section:
        if sec <= painted:
            continue
        else:
            painted = sec + m - 1
            count += 1
    return count

print(solution(8, 4, [2, 3, 6]))