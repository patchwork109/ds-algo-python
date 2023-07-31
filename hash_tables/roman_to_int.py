# https://leetcode.com/problems/roman-to-integer/
# 
# 
# s = "III" --> 3

s = "III"
s2 = "LVIII"
s3 = "MCMXCIV"

def roman_to_integer(s):

    roman_num_mapping = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100, 
        "D" : 500,
        "M" : 1000
    }

    special_cases = {
        'IV' : 4,
        'IX' : 9,
        'XL' : 40,
        'XC' : 90,
        'CD' : 400,
        'CM' : 900,
    }

    int_value = 0
    i = 0 
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in special_cases:
            int_value += special_cases[s[i:i + 2]]
            i += 2
        else:
            int_value += roman_num_mapping[s[i]]
            i += 1
    
    return int_value

print(roman_to_integer(s))
print(roman_to_integer(s2))
print(roman_to_integer(s3))
