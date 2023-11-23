from  check_list_sorted import checkListSort
# merge sort (recursive)

def split_list(list):
    half = len(list)//2
    return list[half:], list[:half]

def merge_sort(merge_list1, merge_list2):
    # check and split until sequence size 1 and work back up the stack (recursive)
    if len(merge_list1) > 1:
        a, b = split_list(merge_list1)
        merge_list1 = merge_sort(a, b)
    if len(merge_list2) > 1:
        a, b = split_list(merge_list2)
        merge_list2 = merge_sort(a, b)

    # logic part
    range_size = max(len(merge_list1), len(merge_list2))
    result_list = []
    # go through all elements, i not used
    for i in range(range_size):
        # take highest element and put it in the result list
        if merge_list1[0] > merge_list2[0]:
            result_list.append(merge_list1[0])
            merge_list1.pop(0)
        else:
            result_list.append(merge_list2[0])
            merge_list2.pop(0)

        # if some list is empty (range takes longest size), end the for loop
        if len(merge_list1) == 0 or len(merge_list2) == 0:
            break
    
    # append the list that's not empty yet
    if len(merge_list1) > 0:
        for i in range(len(merge_list1)):
            result_list.append(merge_list1[i])
    elif len(merge_list2) > 0:
        for i in range(len(merge_list2)):
            result_list.append(merge_list2[i])

    # return the merged list
    return result_list

list1 = [5, 7, 3]
list2 = [1, 9, 2]
merged_list = merge_sort(list1, list2)
print(f"{merged_list}       sorted: {checkListSort(merged_list)}")
