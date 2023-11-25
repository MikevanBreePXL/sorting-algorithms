import time
from check_list_sorted import checkListSort
# bubble sort

def bubble_sort(sort_list, direction = "ascending"):
    is_sorted = False
    i = 1
    j = 0
    total_comparisons = 0
    list_loops = 1
    while is_sorted == False:
        # check if swap needed
        #debug/verbose: print(f"Compare: [{sort_list[j]}](L) & [{sort_list[i]}](R)")
        match direction:
            case "ascending":
                if sort_list[i] < sort_list[j]:
                    # Swap!
                    #debug/verbose: print("Swap!")
                    swap_var = sort_list[j]
                    sort_list[j] = sort_list[i]
                    sort_list[i] = swap_var
                total_comparisons += 1
            case "descending":
                if sort_list[i] > sort_list[j]:
                    # Swap!
                    #debug/verbose: print("Swap!")
                    swap_var = sort_list[j]
                    sort_list[j] = sort_list[i]
                    sort_list[i] = swap_var
                total_comparisons += 1
            case _:
                error = ValueError
                error.add_note('direction needs to be default, "ascending" or "descending"')
                raise error

        # if not: next bubble
        #debug/verbose: print(f"Next iteration")
        if i >= len(sort_list) - list_loops:
            # if iterators are at the end of the list
            
            #check if sorted
            #debug/verbose: print(f"Sorted? {checkListSort(sort_list)}\n{sort_list}")
            is_sorted = checkListSort(sort_list)

            # if not sorted: loop back around (first bubble)
            #debug/verbose: print("Looped back to start of the list")
            i = 1
            j = 0
            list_loops += 1
        else:
            # increment iterators by 1 (next bubble)
            i += 1
            j += 1
    # if sorted: return the sorted list
    return sort_list, total_comparisons