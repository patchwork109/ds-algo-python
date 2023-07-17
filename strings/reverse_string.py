# https://leetcode.com/problems/reverse-string/
# Create a function that reverses a string
# 'Hi, my name is Sam!' -> '!maS si eman ym ,iH'

greeting = 'Hi, my name is Sam!'

def reverse_string(any_string): 
    reversed_string = any_string[::-1]
    return reversed_string

print(reverse_string(greeting))


def reverse_string2(any_string):
    if not isinstance(any_string, str) or len(any_string) < 2:
        return "Provide a string with 2 or more characters."
    
    reversed_string = []
    for i in range(len(any_string) - 1, -1, -1):
        reversed_string.append(any_string[i])
    concatenated_reversed_string = ''.join(reversed_string)
    return concatenated_reversed_string

print(reverse_string2(greeting))


# def reverse_string3(s):
#     left, right = 0, len(s) - 1
        
#     # Loop until the pointers meet at the center
#     while left < right:
#         # Swap the characters at the left and right indices
#         s[left], s[right] = s[right], s[left]
            
#         # Increment left and decrement right
#         left += 1
#         right -= 1

# print(reverse_string3(greeting))



greeting_string = 'Hello, my name is Sam!'

def reverse_this_string(any_string):
    reversed_string = list(reversed(any_string))
    return ''.join(reversed_string)

print(reverse_this_string(greeting_string))


def reverse_this_string2(any_string):
    reversed_string = any_string[::-1]
    return reversed_string

print(reverse_this_string2(greeting_string))


def reverse_this_string3(any_string):
    if not isinstance(any_string, str):
        return 'this is not a string'
    elif len(any_string) < 2:
        return any_string
    
    reversed_string = []
    for index in range(len(any_string) - 1, -1, -1):
        reversed_string.append(any_string[index])
        concatenated_string = ''.join(reversed_string)
    return concatenated_string

print(reverse_this_string3('m'))


