# https://leetcode.com/problems/maximum-subarray/description/
# Create a function that finds the subarray with the largest sum, and return its sum.
# nums = [-2,1,-3,4,-1,2,1,-5,4] -> 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

nums = [-2,1,-3,4,-1,2,1,-5,4]

def maximum_subarray(num_list):
    max_sum = num_list[0]
    current_sum = num_list[0]

    for num in num_list[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum   


print(maximum_subarray(nums))