# https://leetcode.com/problems/valid-palindrome/
# A phrase is a palindrome if, after converting all uppercase 
# letters into lowercase letters and removing all non-alphanumeric 
# characters, it reads the same forward and backward. Alphanumeric 
# characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
# s = "A man, a plan, a canal: Panama" --> true
# Explanation: "amanaplanacanalpanama" is a palindrome.

s = "A man, a plan, a canal: Panama"
s2 = "race a car"

def valid_palindrome(s):
    lowercase_string = s.lower()

    converted_string = []
    for char in lowercase_string:
        if char.isalnum():
            converted_string.append(char)
    
    concatenated_string = ''.join(converted_string)
    
    return concatenated_string[:len(concatenated_string)] == concatenated_string[::-1]


print(valid_palindrome(s))
print(valid_palindrome(s2))