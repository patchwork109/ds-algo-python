# Create a function that merges two sorted arrays (lists)
# [0, 3, 4, 31], [4, 6, 30] -> [0, 3, 4, 4, 6, 30, 31]

list1 = [0, 3, 4, 31]
list2 = [4, 6, 30]

def merged_sorted(any_list1, any_list2):
    combined_list = any_list1 + any_list2
    sorted_list = sorted(combined_list)
    return sorted_list
    
print(merged_sorted(list1, list2))


def merged_sorted2(any_list1, any_list2):
    sorted_list = []
    i = 0
    j = 0

    while i < len(any_list1) and j < len(any_list2):
        if any_list1[i] < any_list2[j]:
            sorted_list.append(any_list1[i])
            i += 1
        else:
            sorted_list.append(any_list2[j])
            j += 1
    
    if i < len(any_list1):
        sorted_list.append(any_list1[i])
        i += 1

    if j < len(any_list2):
        sorted_list.append(any_list2[j])
        j += 1

    return sorted_list

print(f"This is 2: {merged_sorted2(list1, list2)}")


def merge_sorted3(any_list1, any_list2):
    sorted_list = []
    i = 0
    j = 0
    for _ in any_list1 + any_list2:
        if i >= len(any_list1):
            sorted_list.append(any_list2[j])
            j += 1
            print(i)
        elif j >= len(any_list2):
            sorted_list.append(any_list1[i])
            i += 1
            print(i)
        elif any_list1[i] <= any_list2[j]:
            sorted_list.append(any_list1[i])
            i += 1
            print(i)
        else:
            sorted_list.append(any_list2[j])
            j += 1
    
    return sorted_list

print(merge_sorted3(list1, list2))



def merge_sorted_lists(list1, list2):
    sorted_list = []
    i = 0
    j = 0
    for num in list1 + list2:
        if i >= len(list1):
            sorted_list.append(list2[j])
            j += 1
        elif j >= len(list2):
            sorted_list.append(list1[i])
            i += 1
        elif list1[i] <= list2[j]:
            sorted_list.append(list1[i])
            i += 1
        elif list2[j] <= list1[i]:
            sorted_list.append(list2[j])
            j += 1

    return sorted_list


# Create a function that merges two sorted arrays (lists)
# [0, 3, 4, 31], [4, 6, 30] -> [0, 3, 4, 4, 6, 30, 31]

list9 = [0, 3, 4, 31]
list10 = [4, 6, 30]


def merge_sorted_lists5(list1, list2):
    pass

print(f"I'm the newest output: {merge_sorted_lists5(list9,list10)}")


