# https://leetcode.com/problems/move-zeroes/description/
# Create a function that moves all 0's to the end of it while 
# maintaining the relative order of the non-zero elements
# Must do this in-place without making a copy of the array
# nums = [0,1,0,3,12] -> [1,3,12,0,0]

nums = [0,1,0,3,12]
nums2 = [0,1,0,3,13]
nums3 = [0,1,0,3,18]

def move_zeros(num_list):
    i = 0
    for num in num_list:
        if num != 0:
            num_list[i] = num
            i += 1
            print(f"Num is {num} and i is {i}")
            print(f"The num list is now {num_list}")
    
    while i < len(num_list):
        num_list[i] = 0
        i += 1
        print(f"The num list is now {num_list}")
    
    return num_list
    
print(move_zeros(nums))



def move_zeros2(num_list):
    i = 0
    for j in range(len(num_list)):
        if num_list[j] != 0:
            print(f"j is {num_list[j]} and i is {num_list[i]}")
            num_list[i], num_list[j] = num_list[j], num_list[i]
            print(f"The num list is now {num_list}")
            i += 1
    return num_list

print(move_zeros2(nums2))


def move_zeros3(num_list):
    i = 0
    for j in range(len(num_list)):
        if num_list[j] != 0:
            num_list[i], num_list[j] = num_list[j], num_list[i]
            i += 1

    return num_list

print(move_zeros3(nums3))



# other approaches assuming you can create another data structure

nums5 = [0,1,0,3,12]
nums6 = [0,1,0,3,13]
nums7 = [0,1,0,3,18]
nums8 = [7,6,4,0,5]

def move_zeros4(nums):
    num_zeros_end = []

    for num in nums:
        if num != 0:
            num_zeros_end.append(num)
    
    while len(num_zeros_end) < len(nums):
        num_zeros_end.append(0)
    
    return num_zeros_end

print(move_zeros4(nums5))
print(move_zeros4(nums6))

def move_zeros5(nums):
    sorted_nums = sorted(nums)
    reversed_nums = sorted_nums[::-1]
    
    return reversed_nums

print(move_zeros5(nums7))
print(move_zeros5(nums8))