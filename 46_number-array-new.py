def solution(s):
    myDict = {"one": "1", "two": "2", "three": "3", "four": "4", 
             "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for word, digit in myDict.items():
        s = s.replace(word, digit)
        answer = int(s)       
    return answer
  
print(solution("one4seveneight"))      
        
 
              