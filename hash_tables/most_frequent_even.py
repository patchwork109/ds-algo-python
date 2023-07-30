# https://leetcode.com/problems/most-frequent-even-element/description/
# Given an integer array nums, return the most frequent even element.
# If there is a tie, return the smallest one. If there is no such 
# element, return -1.
# nums = [0,1,2,2,4,4,1] --> 2
# nums = [4,4,4,9,2,4] --> 4
# nums = [29,47,21,41,13,37,25,7] --> -1

nums = [0,1,2,2,4,4,1]
nums2 = [4,4,4,9,2,4] 
nums3 = [29,47,21,41,13,37,25,7] 

def most_frequent_even(nums):
    evens = {}

    for num in nums:
        if num % 2 == 0 and num not in evens:
            evens[num] = 1
        elif num % 2 == 0 and num in evens:
            evens[num] += 1

    if not evens:
        return -1

    smallest_max_even = 0
    result = -1
    for key, value in evens.items():
        if value > smallest_max_even:
            smallest_max_even = value
            result = key
        elif value == smallest_max_even and key < result:
            result = key
            
    return result

print(most_frequent_even(nums))
print(most_frequent_even(nums2))
print(most_frequent_even(nums3))