from bubble_sort import bubble_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from shuffle_list import shuffle_fischer_yates
from shuffle_list import shuffle_naive

# scroll all the way down
# scroll all the way down

def shuffle_using_Fischer_Yates(any_list):
    shuffled_list = shuffle_fischer_yates(any_list)
    print("List size: "+ len(shuffled_list))
    print(f"shuffled by Fischer-Yates shuffle:\n{shuffled_list}\n")
    return shuffled_list

def shuffle_using_naive(any_list):
    shuffled_list = shuffle_naive(any_list)
    print("List size: " + len(shuffled_list))
    print(f"shuffled by Naive shuffle:\n{shuffled_list}\n")
    return shuffled_list


def write_sort_output(original_list, sorted_list, comparison_amount):
    print(f"Comparisons taken: {comparison_amount}")
    print("  - " + original_list)
    print("    -> " + sorted_list)

def sort_using_bubble_sort(unsorted_list, order_direction = "descending"):
    sorted_list, comparison_amount = bubble_sort(unsorted_list, order_direction)
    write_sort_output(unsorted_list, sorted_list, comparison_amount)

def sort_using_insertion_sort(unsorted_list, order_direction = "descending"):
    sorted_list, comparison_amount = insertion_sort(unsorted_list, order_direction)
    write_sort_output(unsorted_list, sorted_list, comparison_amount)

def sort_using_merge_sort(unsorted_list, order_direction = "descending"):
    sorted_list, comparison_amount = merge_sort(unsorted_list, order_direction)
    write_sort_output(unsorted_list, sorted_list, comparison_amount)




list_to_shuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffled_list = shuffle_using_Fischer_Yates(list_to_shuffle)
# shuffled_list = shuffle_using_naive(list_to_shuffle)

sort_using_bubble_sort(shuffled_list)
# sort_using_insertion_sort(shuffled_list)
# sort_using_merge_sort(shuffled_list)