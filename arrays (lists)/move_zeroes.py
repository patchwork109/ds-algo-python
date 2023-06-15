# https://leetcode.com/problems/move-zeroes/description/
# Create a function that moves all 0's to the end of it while 
# maintaining the relative order of the non-zero elements
# Must do this in-place without making a copy of the array
# nums = [0,1,0,3,12] -> [1,3,12,0,0]

nums = [0,1,0,3,12]
nums2 = [0,1,0,3,13]

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







