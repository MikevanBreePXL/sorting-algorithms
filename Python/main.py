from bubble_sort import bubble_sort
from shuffle_list import shuffle_fischer_yates

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List size: {len(sorted_list)}\n{sorted_list}\n")

shuffled_list = shuffle_fischer_yates(sorted_list)
print(f"shuffled by Fischer-Yates shuffle:\n{shuffled_list}")

# bubble sort
bubble_sorted_list, comparisons_taken = bubble_sort(shuffled_list)
print(f"sorted list by using merge sort:\n{bubble_sorted_list}")
print(f"Comparisons taken: {comparisons_taken}\n")