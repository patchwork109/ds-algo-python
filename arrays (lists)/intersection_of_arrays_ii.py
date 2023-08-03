# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and 
# you may return the result in any order.
# nums1 = [1,2,2,1], nums2 = [2,2] --> [2,2]
# nums1 = [4,9,5], nums2 = [9,4,9,8,4] --> [4,9]


nums1 = [1,2,2,1]
nums2 = [2,2]

nums3 = [4,9,5]
nums4 = [9,4,9,8,4]

def intersection_two_arrays(nums1, nums2):
    intersection = []
    nums1_count = {}

    for num in nums1:
        if num not in nums1_count:
            nums1_count[num] = 1
        else:
            nums1_count[num] += 1
    
    for num in nums2:
        if num in nums1_count and nums1_count[num] != 0:
            intersection.append(num)
            nums1_count[num] -= 1

    return intersection

print(intersection_two_arrays(nums1, nums2))
print(intersection_two_arrays(nums3, nums4))