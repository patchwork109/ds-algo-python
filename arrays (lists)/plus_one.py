# https://leetcode.com/problems/plus-one/
# Create a function that increments a given large integer by one where
# the large integer is represented as an integer array. The digits are 
# ordered from most significant to least significant in left-to-right order.
# digits = [1,2,3] -> [1,2,4]
# digits = [4,5,8,9] -> [4,5,9,0]

# Turn digits into one large integer
# Increase the large integer by 1
# Turn the large integer back into an integer array

digits = [1,2,3]
digits2 = [4,5,8,9]

def plus_one(int_list):
    string_list = []

    for num in int_list:
        string_list.append(str(num))

    concatenated_str = ''.join(string_list)
    concatenated_num = int(concatenated_str)
    incremented_num = concatenated_num + 1

    incremented_num_str = str(incremented_num)
    list_incremented_num_str = list(incremented_num_str)

    new_digit_list = []
    for num_str in list_incremented_num_str:
        new_digit_list.append(int(num_str))
  
    return new_digit_list


print(plus_one(digits))





