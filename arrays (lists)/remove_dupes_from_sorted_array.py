# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
# Given an integer array nums sorted in non-decreasing order, remove some duplicates 
# in-place such that each unique element appears at most twice. The relative order of the 
# elements should be kept the same.
# nums = [1,1,1,2,2,3] --> 5, nums = [1,1,2,2,3,_]
# nums = [0,0,1,1,1,1,2,3,3] --> 7, nums = [0,0,1,1,2,3,3,_,_]

nums = [1,1,1,2,2,3]
nums2 = [0,0,1,1,1,1,2,3,3,3]

def remove_dupes(nums):
    i = 0
    while i < len(nums) - 2:
        if nums[i] == nums[i + 1] and nums[i] != nums[i + 2]:
            i += 1
        elif nums[i] != nums[i + 1]:
            i += 1
        elif nums[i] == nums[i + 1] and nums[i] == nums[i + 2]:
            nums.pop(i + 1)
        else:
            i += 1

    return len(nums)
    
print(remove_dupes(nums))
print(remove_dupes(nums2))


def remove_dupes2(nums):

    for i in range(len(nums) -2, 0, -1):
        if nums[i] == nums[i + 1] and nums[i] == nums[i - 1]:
            nums.pop(i + 1)

    print(nums)
    return len(nums)
    
# print(remove_dupes2(nums))
# print(remove_dupes2(nums2))