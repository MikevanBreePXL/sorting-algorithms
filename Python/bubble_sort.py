import time
from check_list_sorted import checkListSort
# bubble sort

def bubble_sort(sort_list, direction = "ascending"):
    if direction.lower()[0:4] != "desc" and direction.lower()[0:3] != "asc":
        raise Exception('direction needs to be default, "asc(ending)" or "desc(ending)", your value: ' + direction)

    i = 1
    j = 0
    total_comparisons = 0
    list_loops = 1
    while True:
        # check if swap needed
        #debug/verbose: print(f"Compare: [{sort_list[j]}](L) & [{sort_list[i]}](R)")

        if sort_list[i] < sort_list[j]:
            # Swap!
            swap_var = sort_list[j]
            sort_list[j] = sort_list[i]
            sort_list[i] = swap_var
            #debug/verbose: print(f"Swap!\n=> {sort_list}")
        total_comparisons += 1

        # if not: next bubble
        if i >= len(sort_list) - list_loops:
            # if iterators are at the end of the list
            
            #check if sorted
            #debug/verbose: print(f"Sorted? {checkListSort(sort_list)}")
            if checkListSort(sort_list):
                if direction.lower()[0-3] == "des":
                    sort_list = sort_list.reverse()
                
                return sort_list, total_comparisons
                #debug/verbose: print("--- EXITED SUCCESSFULLY ---")
            else:
                # if not sorted: loop back around (first bubble)
                #debug/verbose: print(f"{sort_list}\nLooped back to start of list")
                i = 1
                j = 0
                list_loops += 1
        else:
            # increment iterators by 1 (next bubble)
            #debug/verbose: print(f"Next bubble")
            i += 1
            j += 1