# https://leetcode.com/problems/valid-anagram/
# Write a function where given two strings s and t, return 
# true if t is an anagram of s, and false otherwise.
# s = "anagram", t = "nagaram" --> true
# s = "rat", t = "car" --> false

s = "anagram"
t = "nagaram"

s2 = "rat"
t2 = "car"

def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)

print(valid_anagram(s,t))


def valid_anagram2(s,t):
    if len(s) != len(t):
        return False
    
    s_char_count = {}
    t_char_count = {}

    for char in s:
        if char not in s_char_count:
            s_char_count[char] = 1
        else:
            s_char_count[char] += 1

    for char in t:
        if char not in t_char_count:
            t_char_count[char] = 1
        else:
            t_char_count[char] += 1
    
    if s_char_count == t_char_count:
        return True
    else:
        return False


print(valid_anagram2(s,t))
print(valid_anagram2(s2,t2))

    


