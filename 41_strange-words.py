def solution(s):
    answer = []
    words = s.split(" ") # Split the string into words (preserving spaces)
    for word in words:
        formatted_word = []
        for idx, char in enumerate(word):
            if idx % 2 == 0:
                formatted_word.append(char.upper())
            else:
                formatted_word.append(char.lower())
        answer.append("".join(formatted_word))
        # Join the formatted word and add to answer
        
    return " ".join(answer)  # Rejoin words with spaces

# Test case
print(solution("try hello world"))


def solutions2(s):
    return " ".join(["".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split(" ")])


def solutions3(s):
    return " ".join([
        "".join([
            char.upper() if idx % 2 == 0 else char.lower() 
            for idx, char in enumerate(word)
            ]) 
        for word in s.split(" ")
        ])
    
print(solution3("try hello world everyone"))