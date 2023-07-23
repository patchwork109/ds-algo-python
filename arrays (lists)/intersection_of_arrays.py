# https://leetcode.com/problems/intersection-of-two-arrays/
# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.
# nums1 = [1,2,2,1], nums2 = [2,2] --> [2]
# nums1 = [4,9,5], nums2 = [9,4,9,8,4] --> [4,9] or [9,4]

nums1 = [1,2,2,1]
nums2 = [2,2]

nums3 = [4,9,5]
nums4 = [9,4,9,8,4]

def intersection_of_lists(nums1, nums2):
    ints_in_intersection = []

    for item in nums1 and nums2:
        if item in nums1 and item in nums2 and item not in ints_in_intersection:
            ints_in_intersection.append(item)

    return ints_in_intersection

print(intersection_of_lists(nums1, nums2))
print(intersection_of_lists(nums3, nums4))


def intersection_of_lists2(nums1, nums2):
    nums1_set = set(nums1)
    nums2_set = set(nums2)

    ints_in_intersection = []

    for item in nums1_set and nums2_set:
        if item in nums1_set and item in nums2_set:
            ints_in_intersection.append(item)

    return ints_in_intersection


print(intersection_of_lists2(nums1, nums2))
print(intersection_of_lists2(nums3, nums4))

