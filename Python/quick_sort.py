import random

def quick_sort_pivot_last(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    #debug/verbose: print(f"Going to quick sort list: {unsorted_list}")
    
    # Create variables for iterating through the list
    pivot_index = len(unsorted_list) - 1
    i_pointer = -1
    j_pointer = 0

    # Quick sort through the list
    while j_pointer < pivot_index:
        comparison_counter += 1
        if unsorted_list[j_pointer] < unsorted_list[pivot_index]:
            i_pointer += 1

            swap_temp = unsorted_list[i_pointer]
            unsorted_list[i_pointer] = unsorted_list[j_pointer]
            unsorted_list[j_pointer] = swap_temp
        j_pointer += 1
    
    # Put pivot back in correct final place
    i_pointer += 1
    swap_temp = unsorted_list[i_pointer]
    unsorted_list[i_pointer] = unsorted_list[pivot_index]
    unsorted_list[pivot_index] = swap_temp
    pivot_index = i_pointer

    #debug/verbose: print(f"- part 1: {unsorted_list[:pivot_index]}")
    #debug/verbose: print(f"- pivot (correct place): {unsorted_list[pivot_index]}")
    #debug/verbose: print(f"- part 2: {unsorted_list[pivot_index + 1:]}")
    #debug/verbose: print(f"New list: {unsorted_list}")
    return quick_sort_pivot_last(unsorted_list[:pivot_index]) + [unsorted_list[pivot_index]] + quick_sort_pivot_last(unsorted_list[pivot_index + 1:])