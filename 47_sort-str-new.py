def solution(strings, n):
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if strings[i][n] > strings[j][n]:
               strings[i], strings[j] = strings[j], strings[i]
            elif strings[i][n] == strings[j][n] and strings[i] > strings[j]:
                strings[i], strings[j] = strings[j], strings[i]
    return strings

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))