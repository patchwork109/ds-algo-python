# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.
# nums = [4,3,2,7,8,2,3,1] --> [5,6]
# nums = [1,1] --> [2]

nums = [4,3,2,7,8,2,3,1]
nums2 = [1,1]


def find_nums(nums):
    set_nums = set(nums)
    missing = []

    for i in range(1,len(nums) + 1):
        if i not in set_nums:
            missing.append(i)

    return missing
    
print(find_nums(nums))
print(find_nums(nums2))