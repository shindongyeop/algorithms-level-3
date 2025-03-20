def solution(t, p):
    answer = 0
    for i in range(0, len(t) - len(p) + 1):
        j = []
        j = int(t[i: i + len(p)])
        if j <= int(p):
                answer += 1
    return answer

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))

def solution2(t, p):
    count = 0
    p_length = len(p)
    t_length = len(t)
    for i in range(t_length - p_length + 1):
        if int(t[i:i + p_length]) <= int(p):
            count += 1
    return count
    
print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))