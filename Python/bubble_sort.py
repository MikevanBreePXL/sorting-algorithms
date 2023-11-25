import time
from check_list_sorted import checkListSort
# bubble sort

def bubble_sort(list1):
    is_sorted = False
    i = 1
    j = 0
    total_comparisons = 0
    list_loops = 1
    while is_sorted == False:
        # check if swap needed
        if list1[i] > list1[j]:
            # Swap!
            swap_var = list1[j]
            list1[j] = list1[i]
            list1[i] = swap_var
        total_comparisons += 1

        #check if sorted
        is_sorted = checkListSort(list1)

        # if not: next bubble
        if i == len(list1) - list_loops:
            # if iterators are at the end of the list, loop back around (first bubble)
            i = 1
            j = 0
            list_loops += 1
        else:
            # increment iterators by 1 (next bubble)
            i += 1
            j += 1
    # if sorted: return the sorted list
    return list1, total_comparisons