def solution(n, m, section):
    count = 0     # Initialize the value of count variable
    painted = 0   # Initialize the value of painted variable
    
    for sec in section:    
        if painted >= sec:  # If the current section is already painted, continue
            continue
          # Calculate the painted area- represent the rightmost position painted so far
        painted = sec + m - 1 
        count += 1            # Count the number of roller stroke so far
        
    return count

print(solution(8, 4, [2, 3, 6]))