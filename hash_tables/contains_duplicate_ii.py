# https://leetcode.com/problems/contains-duplicate-ii/description/
# Given an integer array nums and an integer k, return true if there are two distinct 
# indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# nums = [1,2,3,1], k = 3 --> True
# nums = [1,0,1,1], k = 1 --> True
# nums = [1,2,3,1,2,3], k = 2 --> False

nums = [1,2,3,1]
k = 3

nums2 = [1,0,1,1]
k2 = 1

nums3 = [1,2,3,1,2,3]
k3 = 2

# works, but hits TLE error in Leetcode

def contains_duplicate(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    
    return False

print(contains_duplicate(nums, k))
print(contains_duplicate(nums2, k2))
print(contains_duplicate(nums3, k3))



def contains_duplicate2(nums, k):
    seen_ints = {}

    for index, num in enumerate(nums):
        if num in seen_ints and abs(index - seen_ints[num]) <= k:
            return True
        seen_ints[num] = index

    return False

print(contains_duplicate2(nums, k))
print(contains_duplicate2(nums2, k2))
print(contains_duplicate2(nums3, k3))