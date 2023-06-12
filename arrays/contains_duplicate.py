# Create a function that returns true if any value appears at least twice
# and returns false if every element is distinct.
# nums = [1,2,3,1] -> true

nums = [1,2,3,1,5,6,8,2,2,5]
nums2 = [1,2,3,4]

def contains_dupes(num_list):
    unique_list = []
    for num in num_list:
        if num not in unique_list:
            unique_list.append(num)
            print(f"The unique list is now: {unique_list}")
        else:
            print(f"This {num} is a dupe!")
            return True
    print("No dupes here!")   
    return False

print(contains_dupes(nums))



def contains_dupes2(num_list):
    if len(num_list) != len(set(num_list)):
        print("We have some dupes here!")
        return True
    else:
        print("No dupes here!")
        return False

print(contains_dupes2(nums))



# slight change if you wanted to return the unique list
def contains_dupes3(num_list):
    unique_list = []
    for num in num_list:
        if num not in unique_list:
            unique_list.append(num)
            print(f"The unique list is now: {unique_list}")
        else:
            print(f"This {num} is a dupe!")
    return unique_list

print(contains_dupes3(nums))
