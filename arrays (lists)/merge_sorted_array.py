# https://leetcode.com/problems/merge-sorted-array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two 
# integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 --> [1,2,2,3,5,6]

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

def merge_sorted_array(nums1, nums2, m, n): 
    sorted_list = []

    i = 0
    j = 0
    
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            sorted_list.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            sorted_list.append(nums2[j])
            j +=1

    while j < n:
        sorted_list.append(nums2[j])
        j +=1
    
    return sorted_list

# print(merge_sorted_array(nums1, nums2, m, n))


def merge_sorted_array2(nums1, nums2, m, n): 
    i = 0
    j = 0
    
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            nums1.append(nums2[j])
            j += 1

    while j < n:
        nums1.append(nums2[j])
        j += 1

    return nums1
    

print(merge_sorted_array2(nums1, nums2, m, n))
