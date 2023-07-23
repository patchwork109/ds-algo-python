# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string 
# amongst an array of strings. If there is no common prefix, 
# return an empty string "".
# strings = ["flower","flow","flight"] --> "fl"
# strings = ["dog","racecar","car"] -> ""

strings = ["flower","flow","flight"]
strings2 = ["dog","racecar","car"]

def longest_common_prefix(list_of_strings):
    common_prefix = ""
    min_len = min(len(string) for string in list_of_strings)

    # iterate over every string simultaneously
    for i in range(min_len):
        for string in list_of_strings:
            if string[i] != list_of_strings[0][i]:
                return common_prefix

            print(f"Comparing {list_of_strings[0][i]} at index {i} with string '{string[i]}' in {string}")

        common_prefix += list_of_strings[0][i]
        print(f"Current prefix: {common_prefix}")

    return common_prefix
    
print(longest_common_prefix(strings))
print(longest_common_prefix(strings2))



def longest_common_prefix2(list_of_strings):

    common_prefix = ""
    min_len = min(len(string) for string in list_of_strings)

    for i in range(min_len):
        char = list_of_strings[0][i]

        for string in list_of_strings[1:]:
            if string[i] != char:
                return common_prefix
            
            print(f"Comparing '{char}' at index {i} with '{string[i]}' in string '{string}'")
        
        common_prefix += char
        print(f"Current prefix: {common_prefix}")

    return common_prefix

print(longest_common_prefix2(strings))
print(longest_common_prefix2(strings2))
