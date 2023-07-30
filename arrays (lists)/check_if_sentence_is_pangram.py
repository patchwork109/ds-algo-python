# https://leetcode.com/problems/check-if-the-sentence-is-pangram/
# A pangram is a sentence where every letter of the English alphabet appears 
# at least once. Given a string sentence containing only lowercase English 
# letters, return true if sentence is a pangram, or false otherwise.
# sentence = "thequickbrownfoxjumpsoverthelazydog" --> True
# sentence = "leetcode" --> False

sentence = "thequickbrownfoxjumpsoverthelazydog" 
sentence2 = "leetcode"

def pangram(sentence):
    seen_chars = {}

    for letter in sentence:
        if letter not in seen_chars:
            seen_chars[letter] = 1

    return len(seen_chars) == 26

print(pangram(sentence))
print(pangram(sentence2))



def pangram2(sentence):
    seen_chars = {}

    for letter in sentence:
        if letter not in seen_chars:
            seen_chars[letter] = 1

    count = 0 
    for value in seen_chars.values():
        count += value
    
    return count == 26

print(pangram2(sentence))
print(pangram2(sentence2))

