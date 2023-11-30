import random

def quick_sort_pivot_last(unsorted_list, sort_order="ascending"):
    if sort_order.lower()[0:4] != "desc" and sort_order.lower()[0:3] != "asc":
        raise Exception('direction should be default, "asc(ending)" or "desc(ending)", your value: ' + sort_order)
    
    if len(unsorted_list) < 2:
        return unsorted_list, 0
    #debug/verbose: print(f"Going to quick sort list: {unsorted_list}")
    
    # Create variables for iterating through the list
    pivot_index = len(unsorted_list) - 1
    i_pointer = -1
    j_pointer = 0
    comparison_counter = 0

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
    result_list = []
    
    if sort_order[0:4] == "desc":
        added_list, added_comparisons = quick_sort_pivot_last(unsorted_list[pivot_index + 1:], sort_order)
        result_list.extend(added_list)
        comparison_counter += added_comparisons

        result_list.append(unsorted_list[pivot_index])
        
        added_list, added_comparisons = quick_sort_pivot_last(unsorted_list[:pivot_index], sort_order)
        result_list.extend(added_list)
        comparison_counter += added_comparisons
    else:
        added_list, added_comparisons = quick_sort_pivot_last(unsorted_list[:pivot_index], sort_order)
        result_list.extend(added_list)
        comparison_counter += added_comparisons

        result_list.append(unsorted_list[pivot_index])

        added_list, added_comparisons = quick_sort_pivot_last(unsorted_list[pivot_index + 1:], sort_order)
        result_list.extend(added_list)
        comparison_counter += added_comparisons

    return result_list, comparison_counter