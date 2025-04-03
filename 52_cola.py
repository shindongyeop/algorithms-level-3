def solution(a, b, n):
    answer = 0
    total_colas = 0
    new_colas  = 0
    if n < a:
        return 0
    while n >= a:
        new_colas = (n // a) * b 
        total_colas += new_colas
        n = (n % a) + new_colas 
    answer = total_colas
    return answer