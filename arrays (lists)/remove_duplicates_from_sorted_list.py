# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Create a function that removes the duplicates in place such that 
# each unique element only appears once and returns the number of unique 
# elements when given a list of numbers sorted in increasing order.
# nums = [1,1,2,3] -> k = 3, nums = [1,2,3]

nums = [1,1,2,3]
nums2 = [2,3,4,6,7,7,7,7,9]
nums3 = [7,7,9,9,9,10,10,11,12,14,15]

def remove_duplicates(num_list):
    unique_list = []
    for num in num_list:
        if num not in unique_list:
            unique_list.append(num)

    num_list.clear()
    num_list.extend(unique_list)

    return len(unique_list)

print(remove_duplicates(nums))
print(nums)


def remove_duplicates2(num_list):
    unique_list = []
    for num in num_list:
        if num not in unique_list:
            unique_list.append(num)

    num_list[:] = unique_list
    
    return len(unique_list)

print(remove_duplicates2(nums2))
print(nums2)



