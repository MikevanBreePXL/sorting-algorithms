import time
from check_list_sorted import checkListSort
# bubble sort
# NOT REALISTIC / INEFFICIENT

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



elements = [7, 18, 19, 8, 9, 10, 0, 12, 13, 1, 2, 6, 11, 14, 15, 16, 3, 4, 5, 17, 20]
sorted_list, comparisons = bubble_sort(elements)
print(sorted_list)
print(f"sorted: {checkListSort(sorted_list)}")
print(f"comparisons: {comparisons}")