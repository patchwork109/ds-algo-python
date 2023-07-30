# https://leetcode.com/problems/longest-nice-substring/
# A string s is nice if, for every letter of the alphabet that s contains, 
# it appears both in uppercase and lowercase. For example, "abABB" is nice 
# because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not 
# because 'b' appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. If there 
# are multiple, return the substring of the earliest occurrence. If there are 
# none, return an empty string.

# s = "YazaAay" --> "aAa"
# s = "Bb" --> "Bb"
# s = "c" --> ""

s = "YazaAay" 
s2 = "Bb" 
s3 = "c" 

def longest_nice_substring(s):
    if len(s) <= 1:
        return ""
    
    


print(longest_nice_substring(s))
print(longest_nice_substring(s2))
print(longest_nice_substring(s3))