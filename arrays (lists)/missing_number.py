# https://leetcode.com/problems/missing-number/
# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.
# nums = [3,0,1] --> 2
# nums = [0,1] --> 2
# nums = [9,6,4,2,3,5,7,0,1] --> 8

nums = [3,0,1]
nums2 = [0,1] 
nums3 = [9,6,4,2,3,5,7,0,1]

def missing_number(nums):
    sorted_nums = sorted(nums)

    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i] + 1 != sorted_nums[i + 1]:
            return sorted_nums[i] + 1
    
    if 0 not in sorted_nums:
        return 0
    else:
        return len(sorted_nums)

print(missing_number(nums))
print(missing_number(nums2))
print(missing_number(nums3))

# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.
# nums = [3,0,1] --> 2
# nums = [0,1] --> 2
# nums = [9,6,4,2,3,5,7,0,1] --> 8


def missing_number2(nums):
    sorted_nums = sorted(nums)

    if 0 not in sorted_nums:
        return 0
    elif len(nums) not in sorted_nums:
        return len(nums)
    
    for i in range(len(sorted_nums)):
        if i + 1 < len(sorted_nums) and sorted_nums[i] + 1 != sorted_nums[i + 1]:
            return sorted_nums[i] + 1
    
print(missing_number2(nums))
print(missing_number2(nums2))
print(missing_number2(nums3))