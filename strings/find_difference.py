# https://leetcode.com/problems/find-the-difference/
# You are given two strings s and t. String t is generated by random 
# shuffling string s and then add one more letter at a random position.
# Return the letter that was added to t.
# s = "abcd", t = "abcde" --> "e"
# s = "", t = "y" --> "y"

s = "abcd"
t = "abcde"

s2 = ""
t2 = "y"

def find_difference(s,t):
    char_count_s = {}
    char_count_t = {}

    for char in s:
        if char not in char_count_s:
            char_count_s[char] = 1
        else:
            char_count_s[char] += 1

    for char in t:
        if char not in char_count_t:
            char_count_t[char] = 1
        else:
            char_count_t[char] += 1

    for key, value in char_count_t.items():
        if key not in char_count_s or value != char_count_s[key]:
            return key

print(find_difference(s,t))
print(find_difference(s2,t2))
