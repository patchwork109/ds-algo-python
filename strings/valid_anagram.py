# https://leetcode.com/problems/valid-anagram/
# Write a function where given two strings s and t, return 
# true if t is an anagram of s, and false otherwise.
# s = "anagram", t = "nagaram" --> true
# s = "rat", t = "car" --> false

s = "anagram"
t = "nagaram"

def valid_anagram2(s,t):
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)


print(valid_anagram2(s,t))
    


