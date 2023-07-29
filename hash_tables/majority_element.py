# https://leetcode.com/problems/majority-element/
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than 
# ⌊n / 2⌋ times. You may assume that the majority element always 
# exists in the array.
# nums = [3,2,3] --> 3
# nums = [2,2,1,1,1,2,2] --> 2

nums = [3,2,3]
nums2 = [2,2,1,1,1,2,2]


def majority_element(nums):
    seen_nums = {}

    for num in nums:
        if num not in seen_nums:
            seen_nums[num] = 1
        else:
            seen_nums[num] += 1
    
    for key, value in seen_nums.items():
        if value >= len(nums) / 2:
            return key

print(majority_element(nums))
print(majority_element(nums2))

