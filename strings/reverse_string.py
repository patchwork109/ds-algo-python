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
    # concatenated_reversed_string = ''.join(reversed_string)
    # return concatenated_reversed_string
    return reversed_string

print(reverse_string2(greeting))

# left, right = 0, len(s) - 1
        
#         # Loop until the pointers meet at the center
#         while left < right:
#             # Swap the characters at the left and right indices
#             s[left], s[right] = s[right], s[left]
            
#             # Increment left and decrement right
#             left += 1
#             right -= 1
