# https://leetcode.com/problems/two-sum/description/
# Create a function that returns the indices of two numbers that add up to the target
# Do not use the same element twice
# nums = [2,7,11,15], target = 9 -> [0,1]

nums = [2,7,11,15]
nums2 = [3,3]
target = 9
target2 = 6

def two_sum(num_list, int_target):
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == int_target:
                return [i, j]

print(two_sum(nums, target))


def two_sum2(nums, target):
    numMap = {}

    # Build the hash table
    for i in range(len(nums)):
        numMap[nums[i]] = i

    # Find the complement
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]

    return []  # No solution found

print(two_sum2(nums2, target2))


    
