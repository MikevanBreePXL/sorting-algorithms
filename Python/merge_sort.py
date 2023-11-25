from  check_list_sorted import checkListSort
# merge sort (recursive)

# function to split the list in 2 halfs
def split_list(list):
    half = len(list)//2
    #debug/verbose: print(f"Splitting {list} in half => {list[half:]} & {list[:half]}")
    return list[half:], list[:half]

def merge_sort(input_list1, input_list2, direction="ascending"):
    merge_list1 = input_list1.copy()
    merge_list2 = input_list2.copy()
    comparison_counter = 0

    # check and split until sequence size 1 and work back up the stack (recursive)
    if len(merge_list1) > 1:
        a, b = split_list(merge_list1)
        merge_list1, comparisons_done = merge_sort(a, b, direction)
        comparison_counter += comparisons_done
    if len(merge_list2) > 1:
        a, b = split_list(merge_list2)
        merge_list2, comparisons_done = merge_sort(a, b, direction)
        comparison_counter += comparisons_done

    # logic part
    #debug/verbose: print(f"Merging {merge_list1} & {merge_list2} next")
    range_size = max(len(merge_list1), len(merge_list2))
    result_list = []
    # continue until a list is empty
    while True:
        # take lowest element and put it in the result list
        match direction:
            case "ascending":
                comparison_counter += 1
                if (merge_list1[0] < merge_list2[0]):
                    #debug/verbose: print(f"Adding [{merge_list1[0]}] over [{merge_list2[0]}]")
                    result_list.append(merge_list1[0])
                    merge_list1.pop(0)
                else:
                    #debug/verbose: print(f"Adding [{merge_list2[0]}] over [{merge_list1[0]}]")
                    result_list.append(merge_list2[0])
                    merge_list2.pop(0)
                
            case "descending":
                comparison_counter += 1
                if (merge_list1[0] > merge_list2[0]):
                    #debug/verbose: print(f"Adding [{merge_list1[0]}] over [{merge_list2[0]}]")
                    result_list.append(merge_list1[0])
                    merge_list1.pop(0)
                else:
                    #debug/verbose: print(f"Adding [{merge_list2[0]}] over [{merge_list1[0]}]")
                    result_list.append(merge_list2[0])
                    merge_list2.pop(0)
            case _:
                error = ValueError()
                error.add_note('direction needs to be empty, "ascending" or "descending"')
                raise error

        # if some list is empty (range takes longest size), end the loop
        if len(merge_list1) == 0 or len(merge_list2) == 0:
            #debug/verbose: print("Empty list! appending the other to the end")
            break
    
    # append the list that's not empty yet
    if len(merge_list1) > 0:
        for i in range(len(merge_list1)):
            #debug/verbose: print(f"Appending [{merge_list1[i]}]")
            result_list.append(merge_list1[i])
    if len(merge_list2) > 0:
        for i in range(len(merge_list2)):
            #debug/verbose: print(f"Appending [{merge_list2[i]}]")
            result_list.append(merge_list2[i])

    # return the merged list
    #debug/verbose: print(f"Merged lists: {input_list1} & {input_list2}\n=> {result_list}\n---")
    return result_list, comparison_counter