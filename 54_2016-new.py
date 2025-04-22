def solution(a, b):
    Week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    Months = [0, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 100]
    total_days = sum(Months[:a]) + b - 1
    return Week[total_days % 7]