def solution(a, b):
    Week_days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    Month_days = [0, 31, 29, 31, 30, 31, 30, 31,31, 30, 31, 30, 31]
    Total_days = sum(Month_days[:a]) + b - 1
    return Week_days[Total_days % 7]

print(solution(5, 24))