# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# Given two arrays of strings list1 and list2, find the common strings with 
# the least index sum. A common string is a string that appeared in both 
# list1 and list2. A common string with the least index sum is a common string 
# such that if it appeared at list1[i] and list2[j] then i + j should be the 
# minimum value among all the other common strings.

# Return all the common strings with the least index sum. Return the answer 
# in any order.

# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# --> ["Shogun"]

# list1 = ["happy","sad","good"], list2 = ["sad","happy","good"] --> ["sad","happy"]

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

list3 = ["happy","sad","good"]
list4 = ["sad","happy","good"]


def min_index_sum(list1, list2):
    common_strings = {}
    min_index_sum = float('inf')

    list1_indices = {}
    for index, value in enumerate(list1):
        list1_indices[value] = index
    
    for j, element in enumerate(list2):
        if element in list1_indices:
            index_sum = j + list1_indices[element]

            if index_sum < min_index_sum:
                min_index_sum = index_sum

            common_strings[element] = index_sum

    result = []
    for string, index_sum in common_strings.items():
        if index_sum == min_index_sum:
            result.append(string)

    return result
    
print(min_index_sum(list1, list2))
print(min_index_sum(list3, list4))


# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# --> ["Shogun"]

# list1 = ["happy","sad","good"], list2 = ["sad","happy","good"] --> ["sad","happy"]

def min_index_sum2(list1, list2):

    common_strings = []
    for string in list1 and list2:
        if string in list1 and string in list2:
            common_strings.append(string)

    result = []
    min_index_sum = float('inf')
    for string in common_strings:
        index_sum = list1.index(string) + list2.index(string)  # Calculate the index sum for each common string
        if index_sum <= min_index_sum:  # If the index sum is less than the current minimum, update the result list
            min_index_sum = index_sum
            result.append(string)

    return result

print(min_index_sum2(list1, list2))
print(min_index_sum2(list3, list4))