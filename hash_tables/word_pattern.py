# https://leetcode.com/problems/word-pattern/
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a 
# letter in pattern and a non-empty word in s.

# pattern = "abba", s = "dog cat cat dog" --> True
# pattern = "abba", s = "dog cat cat fish" --> False
# pattern = "aaaa", s = "dog cat cat dog" --> False

pattern = "abba"
s = "dog cat cat dog" 
pattern2 = "abba"
s2 = "dog cat cat fish bird"
pattern3 = "aaaa"
s3 = "dog cat cat dog" 

def word_pattern(pattern, s):
    s_string = s.split(" ")
    
    if len(pattern) != len(s_string):
        return False
    
    if len(set(pattern)) != len(set(s_string)):
        return False
    
    pattern_mapping = {}
    for i in range(len(s_string)):
        if s_string[i] not in pattern_mapping:
            pattern_mapping[s_string[i]] = pattern[i]
        elif pattern_mapping[s_string[i]] != pattern[i]:
            return False
    
    return True

print(word_pattern(pattern,s))
print(word_pattern(pattern2,s2))
print(word_pattern(pattern3,s3))


