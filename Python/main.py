from merge_sort import merge_sort
from shuffle_list import shuffle_fischer_yates

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List size: {len(sorted_list)}\n{sorted_list}\n")

shuffled_list = shuffle_fischer_yates(sorted_list)
print(f"shuffled by Fischer-Yates shuffle:\n{shuffled_list}\n")

half_length = len(shuffled_list)//2
list_half1 = shuffled_list[half_length:]
list_half2 = shuffled_list[:half_length]
merge_sorted_list, comparisons_taken = merge_sort(list_half1, list_half2, "descending")
print(f"sorted list by using merge sort:\n{merge_sorted_list}")
print(f"Comparisons taken: {comparisons_taken}\n")