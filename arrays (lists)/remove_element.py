# https://leetcode.com/problems/remove-element/
# Given an integer array nums and an integer val, remove all occurrences 
# of val in nums in-place. The order of the elements may be changed. Then 
# return the number of elements in nums which are not equal to val.

# nums = [3,2,2,3], val = 3 --> 2, nums = [2,2,_,_]
# nums = [0,1,2,2,3,0,4,2], val = 2 --> 5, nums = [0,1,4,0,3,_,_,_]

nums = [3,2,2,3]
val = 3

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2


def remove_element(nums, val):
    # using a while loop (instead of for loop) helps avoid issues while 
    # interating over the array and modifying it in place
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            print(nums)
        else:
            i += 1
    
    return len(nums)


print(remove_element(nums,val))
print(remove_element(nums2,val2))