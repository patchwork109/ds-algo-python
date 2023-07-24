# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters 
# '(', ')', '{', '}', '[' and ']', determine if the 
# input string is valid.

# An input string is valid if:
# -- Open brackets must be closed by the same type of brackets.
# -- Open brackets must be closed in the correct order.
# -- Every close bracket has a corresponding open bracket of the same type.

# s = "()" --> true
# s = "()[]{}" --> true
# s = "(]" --> false

s = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "{[]}"

def valid_parentheses(s):
    for i in range(len(s)):
        if s[i] == "(" and s[i + 1] != ")":
            return False
        elif s[i] == "[" and s[i + 1] != "]":
            return False
        elif s[i] == "{" and s[i + 1] != "}":
            return False
        else: 
            return True
        
# this solution only works when the opening and closing brackets
# are next to each other; doesn't handle cases like this "{[]}"
            
print(valid_parentheses(s))
print(valid_parentheses(s2))
print(valid_parentheses(s3))
print(valid_parentheses(s4))



def valid_parentheses2(s):
    stack = []
    close_to_open_dict = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }

    for bracket in s:
        if bracket in close_to_open_dict:
            if stack and stack[-1] == close_to_open_dict[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)

    if not stack:
        return True
    else:
        return False


print(valid_parentheses2(s))
print(valid_parentheses2(s2))
print(valid_parentheses2(s3))
print(valid_parentheses2(s4))



def valid_parentheses3(s):
    stack = []
    bracket_dict = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }

    for bracket in s:
        if bracket in '([{':
            stack.append(bracket)
        elif bracket in ')]}':
            if not stack or stack[-1] != bracket_dict[bracket]:
                return False
            else:
                stack.pop()
    
    # need this portion b/c if the stack isn't empty, then that means
    # there are unclosed brackets
    if not stack:
        return True
    else:
        return False

print(valid_parentheses3(s))
print(valid_parentheses3(s2))
print(valid_parentheses3(s3))
print(valid_parentheses3(s4))

