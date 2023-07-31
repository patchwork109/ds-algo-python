# https://leetcode.com/problems/rotate-array/description/
# Create a function that rotates an array to the right by k steps, where k is non-negative
# nums = [1,2,3,4,5,6,7], k = 3 -> [5,6,7,1,2,3,4]
# Explanation:
# - rotate 1 steps to the right: [7,1,2,3,4,5,6]
# - rotate 2 steps to the right: [6,7,1,2,3,4,5]
# - rotate 3 steps to the right: [5,6,7,1,2,3,4]

nums = [1,2,3,4,5,6,7]
nums2 = [1,2,3,4,5,6,7]
nums3 = [1,2,3,4,5,6,7]
k = 5

def rotate(num_list, int_step):
    num_list.reverse()
    num_list[int_step:] = num_list[:int_step - 1:-1]
    num_list[:int_step] = num_list[int_step - 1::-1]
    return num_list

print(rotate(nums, k))


def rotate2(num_list, int_step):
    for _ in range(int_step):
        last_element = num_list[-1]
        for i in range(len(num_list) - 1, 0, -1):
            num_list[i] = num_list[i -1]
        num_list[0] = last_element
    return num_list


print(rotate2(nums2, k))


def rotate3(nums, k):
    k = k % len(nums)
    print(nums[-k:])
    print(nums[:-k])

    print(nums[k:])
    print(nums[:k])

    nums[:] = nums[-k:] + nums[:-k]

    return nums

print(rotate3(nums3, k))
