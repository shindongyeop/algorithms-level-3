def solution(a, b):
    total_days = 0
    days_of_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = sum(days_in_month[:a]) + b - 1  
    return days_of_week[total_days % 7]

print(solution(5, 24))