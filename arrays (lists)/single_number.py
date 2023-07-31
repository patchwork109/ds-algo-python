# https://leetcode.com/problems/single-number/
# Create a function where given a non-empty array of integers nums, 
# every element appears twice except for one. Find that single one.
# Implement a solution with a linear runtime complexity and use 
# only constant extra space.
# nums = [4,1,2,1,2] -> 4


nums = [4,1,2,1,2]
nums2 = [4,1,2,1,2,4,3]
nums_set = set(nums)


def single_number(num_list):
    for num in num_list:
        if num_list.count(num) == 1:
            return num
        
print(single_number(nums))



def single_number2(num_list):
    result = 0

    for num in num_list:
        result ^= num

    return result
        
print(single_number2(nums))



def single_number3(num_list):
    num_list.sort()
    num_list.append(0)
    
    i = 0
    while i < len(num_list):
        if num_list[i] != num_list[i+1]:
            return num_list[i]
        else:
            i += 2

        
print(single_number3(nums))


def single_number4(nums):
    num_count = {}

    for num in nums:
        if num not in num_count:
            num_count[num] = 1
        else:
            num_count[num] += 1
    
    for key, value in num_count.items():
        if value == 1:
            return key
    
print(single_number4(nums2))