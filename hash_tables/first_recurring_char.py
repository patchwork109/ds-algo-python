# Write a function where given a list find the first recurring character
# and return that character. If there are no recurring characters, 
# return None.
# int_list = [2,5,1,2,3,5,1,2,4] --> 2

int_list = [2,5,1,2,3,5,1,2,4]
int_list2 = [2,1,1,2,3,5,1,2,4]
int_list3 = [2,3,4,5]

def first_recurring_char(int_list):
    seen_list = []
    for each_int in int_list:
        if each_int not in seen_list:
            seen_list.append(each_int)
        else:
            return each_int
    
    return None


print(first_recurring_char(int_list))
print(first_recurring_char(int_list2))
print(first_recurring_char(int_list3))


def first_recurring_char2(int_list):
    seen_ints_dict = {}

    for each_int in int_list:
        if each_int in seen_ints_dict:
            return each_int
        else:
            seen_ints_dict[each_int] = True
    
    return None

print(first_recurring_char2(int_list))
print(first_recurring_char2(int_list2))
print(first_recurring_char2(int_list3))


def first_recurring_char3(int_list):
    seen_chars = []

    for num in int_list:
        if num not in seen_chars:
            seen_chars.append(num)
        else:
            return num
    
    return None

print(first_recurring_char3(int_list))
print(first_recurring_char3(int_list2))
print(first_recurring_char3(int_list3))


def first_recurring_char4(int_list):
    seen_chars = {}

    for num in int_list:
        if num not in seen_chars:
            seen_chars[num] = 1
        else:
            return num
        
    return None

print(first_recurring_char4(int_list))
print(first_recurring_char4(int_list2))
print(first_recurring_char4(int_list3))