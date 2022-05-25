# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    if(sorted(s1)== sorted(s2)):
        answer = True
    else:
        answer = False

    return answer
s1 ="heart"
s2 ="earth"
find_anagram(s1, s2)
print(find_anagram(s1, s2))