def solution(n, m, section):
    count = 0    # Initialize roller stroke couint
    painted = 0  # represents the right-most position pointed so far
    
    for sec in section:
        # If the current section is already painted, skip it   
        if sec <= painted:
            continue
    
    # If the current section is unpainted, use the roller here
        painted = sec + m - 1  # paint from sec to (sec + m -1)
        count += 1             # Increase the roller stroke count
    
    return count
# Testing examples provided
print(solution(8, 4, [2, 3, 6]))  # Output: 2
