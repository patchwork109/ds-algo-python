# https://leetcode.com/problems/first-unique-character-in-a-string/
# Given a string s, find the first non-repeating character in it 
# and return its index. If it does not exist, return -1.
# s = "leetcode" --> 0
# s = "loveleetcode" --> 2
# s = "aabb" --> -1

s = "leetcode"
s2 = "loveleetcode"
s3 = "aabb"

def first_unique_char(any_string):
    char_count = {}

    for char in any_string:
        char_count[char] = char_count.get(char, 0) + 1

    for index, char in enumerate(any_string):
        if char_count[char] == 1:
            return index
        
    return -1

print(first_unique_char(s))
print(first_unique_char(s2))
print(first_unique_char(s3))


def first_unique_char2(s):
    seen_char_count = {}

    for char in s:
        if char not in seen_char_count:
            seen_char_count[char] = 1
        else:
            seen_char_count[char] += 1
    
    for index, char in enumerate(s):
        if seen_char_count[char] == 1:
            return index
    
    return -1

print(first_unique_char2(s))
print(first_unique_char2(s2))
print(first_unique_char2(s3))



def first_unique_char3(s):
    seen_char_count = {}

    for i in range(len(s)):
        if s[i] not in seen_char_count:
            seen_char_count[s[i]] = 1
        else:
            seen_char_count[s[i]] += 1

    for i in range(len(s)):
        if seen_char_count[s[i]] == 1:
            return i
        
    return -1

print(first_unique_char3(s))
print(first_unique_char3(s2))
print(first_unique_char3(s3))