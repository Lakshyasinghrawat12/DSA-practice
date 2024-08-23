from typing import List, Optional

def solution(words: List[str]):

    set1= set("qwertyuiop")
    set2= set("asdfghjkl")
    set3= set("zxcvbnm")
    result= []


    for word in words:
        lowercase_word= set(word.lower())

        if lowercase_word.issubset(set1) or lowercase_word.issubset(set2) or lowercase_word.issubset(set3):
            result.append(word)

    return result


words = ["Hello","Alaska","Dad","Peace"]

print(solution(words))