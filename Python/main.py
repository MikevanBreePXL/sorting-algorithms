import time

from bubble_sort import bubble_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort_pivot_last
from bogo_sort import bogo_sort

from shuffle_list import shuffle_fischer_yates
from shuffle_list import shuffle_naive

# scroll all the way down
# scroll all the way down

def shuffle_using_Fischer_Yates(any_list):
    shuffled_list = shuffle_fischer_yates(any_list)
    print(f"List size: {len(shuffled_list)}")
    print(f"shuffled by Fischer-Yates shuffle:\n{shuffled_list}\n")
    return shuffled_list

def shuffle_using_naive(any_list):
    shuffled_list = shuffle_naive(any_list)
    print(f"List size: {len(shuffled_list)}")
    print(f"shuffled by Naive shuffle:\n{shuffled_list}\n")
    return shuffled_list

def write_sort_output(original_list, sorted_list, comparison_amount, start_time, end_time):
    print(f"Sorted list:\n{original_list}")
    print(f"    -> {sorted_list}")
    print(f"Comparisons taken: {comparison_amount}")
    print(f"Time taken: {end_time - start_time}")



list_to_shuffle = list(range(1, 7+1))

# shuffled_list = shuffle_using_naive(list_to_shuffle)
shuffled_list = shuffle_using_Fischer_Yates(list_to_shuffle)
# shuffled_list = [2, 1, 3, 4, 6, 7]

start_time = time.perf_counter()
sorted_list, comparison_amount = insertion_sort(shuffled_list, "ascending")
# sort_using_insertion_sort(shuffled_list)
# sort_using_merge_sort(shuffled_list)
end_time = time.perf_counter()



# print info
print(sorted_list)
print(f"Comparisons taken: {comparison_amount}")
print("{:.4f}".format(end_time - start_time) + " secs")