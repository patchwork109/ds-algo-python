# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without 
# repeating characters.
# s = "abcabcbb" --> 3
# s = "bbbbb" --> 1
# s = "pwwkew" --> 3

s = "abcabcbb"
s2 = "bbbbb" 
s3 = "pwwkew" 

def longest_substring(s):
    char_set = set()
    left = 0
    result = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            print(f"Inside the while loop: s[right] is {s[right]} and char_set is {char_set}")
        char_set.add(s[right])
        print(f"Outside while loop: char_set is {char_set}")
        result = max(result, right - left + 1)
        print(f"Result is {result}")
    
    return result

print(longest_substring(s))
# print(longest_substring(s2))
# print(longest_substring(s3))

