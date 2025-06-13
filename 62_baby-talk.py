def solution(babbling):
    count = 0
    possible_words = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for element in possible_words:
            if element == word:
                count += 1
                print(f'count for element == word: {count}')
            else:
                while element in word:
                    word = word.replace(element, "")
                    if word == element:
                        break
                        count += 1
    
    return count
    
print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))