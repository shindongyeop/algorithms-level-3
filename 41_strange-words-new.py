def solution(s):
    answer = [] # initialize an empty list to store the formatted words
    s = s.split(" ") # split the string into words
    for word in s: # Iterating through each word
        format = []  # Initialize an empty list to store the formatted characters
        print(f'word = {word} and s = {s}')
        for i, chr in enumerate(word): # Iterate through each character in the word
            print(f'i = {i} and chr = {chr}')
            if i % 2 == 0: # If the index is even
                format.append(chr.upper()) # append the uppercase character
                print(f'chr = {chr.upper()}')
            else: # If the index is odd
                format.append(chr.lower()) # append the lowercase character
                print(f'chr = {chr.lower()}')
        word = "".join(format) # Join the formatted characters to form the word
        print(f'word: {word}')
        answer.append(word)  # append the formatted word to the answer list
        print(f'answer = {answer}')
    return " ".join(answer) # Join the formatted words with spaces
         
    


print(solution("try hello world"))

