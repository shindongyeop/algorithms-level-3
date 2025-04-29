def solution (answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    for i, answer in enumerate(answers):
        if answer == student1[i % len(student1)]:
            scores[0] += 1
        if answer == student2[i % len(student2)]:
            scores[1] += 1
        if answer == student3[i % len(student3)]:
            scores[2] += 1
    max_score = max(scores)
    
    result = []
    for i, score in enumerate(scores):
        if score == max_score:
            result.append(i + 1)
            
    return result


print(solution([1,2,3,4,5]))


        
        
        
# rules for naming variables:
# 1. Use lowercase letters and underscores to separate words (e.g., `max_score`, `my_max_score`).
# 2. camelCase is typically used for variable names in Python (e.g., `studentScores`, `myVariableName`).
# 3. Use descriptive names that convey the purpose of the variable (e.g., `student_scores`).
