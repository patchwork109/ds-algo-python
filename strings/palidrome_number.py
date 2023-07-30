# https://leetcode.com/problems/palindrome-number/
# Given an integer x, return true if x is a palindrome, and false otherwise.
# x = 121 --> True
# x = -121 --> False
# x = 10 --> False

x = 121
x2 = -121
x3 = 10

def palindrome_number(x):
    # need to convert this to a string in order to do the reverse comparison
    int_string = str(x)

    return int_string == int_string[::-1]

print(palindrome_number(x))
print(palindrome_number(x2))
print(palindrome_number(x3))