def solution(sizes):
    max_height = 0
    max_width = 0
    for width, height in sizes:
        # print(f'width = {width} and height = {height}')
        width, height = max(width, height), min(width, height)
        # print(f'revised width = {width}')
        # print(f'revised height = {height}')
        max_width = max(width, max_width)
        # print(f'max_width = {max_width}')
        max_height = max(height, max_height)
        # print(f'max_height = {max_height}')
    return max_width * max_height  
    
    
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) # Output 4000
print(solution([[10,7], [12,3],[8,15],[14,7],[5,15]])) # Output 120