# https://leetcode.com/problems/squares-of-a-sorted-array/
# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in 
# non-decreasing order.
# nums = [-4,-1,0,3,10] --> [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

nums = [-4,-1,0,3,10]
nums2 = [-7,-3,2,3,11]


def squares_sorted(nums):
    squared_list = []

    for num in nums:
        squared_list.append(num**2)

    for i in range(len(squared_list) - 1):
        if squared_list[i] >= squared_list[i+1]:
            squared_list[i], squared_list[i+1] = squared_list[i+1], squared_list[i]
            

        for j in range(len(squared_list) - 1):
            if squared_list[j] >= squared_list[j+1]:
                squared_list[j], squared_list[j+1] = squared_list[j+1], squared_list[j]

    return squared_list

# This solution works, but gets a TLE error on LeetCode b/c of nested loops
# print(squares_sorted(nums))
# print(squares_sorted(nums2))



def squares_sorted2(nums):
    squared_list = []

    for num in nums:
        squared_list.append(num**2)

    squared_sorted_list = sorted(squared_list)

    return squared_sorted_list

# This works, but uses the built in sorted function (vs writing our own sort algo)
# print(squares_sorted2(nums))
# print(squares_sorted2(nums2))


def squares_sorted3(nums):
    squared_sorted_list = []
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left]**2 > nums[right]**2:
            squared_sorted_list.append(nums[left]**2)
            left += 1
        else:
            squared_sorted_list.append(nums[right]**2)
            right -= 1
    
    return squared_sorted_list[::-1]

print(squares_sorted3(nums))
print(squares_sorted3(nums2))


def squares_sorted4(nums):
    left = 0 
    right = len(nums) - 1
    squares_sorted_list = []

    while left <= right:
        if nums[left]**2 > nums[right]**2:
            squares_sorted_list.append(nums[left]**2)
            left += 1
        else:
            squares_sorted_list.append(nums[right]**2)
            right -= 1
    
    return squares_sorted_list[::-1]

print(f"This is #4: {squares_sorted4(nums)}")


