from  check_list_sorted import checkListSort
# merge sort (recursive)

def merge_sort(input_list, direction="ascending"):
    if direction.lower()[0:4] != "desc" and direction.lower()[0:3] != "asc":
        raise Exception('direction should be default, "asc(ending)" or "desc(ending)", your value: ' + direction)

    half = len(input_list)//2
    input_half1 = input_list[:half]
    input_half2 = input_list[half:]
    #debug/verbose: print(f"Splitting {input_list} => {input_half1} & {input_half2}")
    merge_list1 = input_half1.copy()
    merge_list2 = input_half2.copy()
    comparison_counter = 0

    # check and split until sequence size 1 and work back up the stack (recursive)
    if len(merge_list1) > 1:
        merge_list1, comparisons_done = merge_sort(merge_list1, direction)
        comparison_counter += comparisons_done
    if len(merge_list2) > 1:
        merge_list2, comparisons_done = merge_sort(merge_list2, direction)
        comparison_counter += comparisons_done
    

    # logic part
    #debug/verbose: print(f"Merging {merge_list1} & {merge_list2} next")
    result_list = []
    # continue until a list is empty
    while True:
        # take lowest element and put it in the result list
        comparison_counter += 1
        if (merge_list1[0] < merge_list2[0]):
            result_list.append(merge_list1[0])
            #debug/verbose: print(f"Adding [{merge_list1[0]}] over [{merge_list2[0]}] => {result_list}")
            merge_list1.pop(0)
        else:
            result_list.append(merge_list2[0])
            #debug/verbose: print(f"Adding [{merge_list2[0]}] over [{merge_list1[0]}] => {result_list}")
            merge_list2.pop(0)

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

    # flip the list if direction is set to descending
    if (direction.lower()[0:4] == "desc"):
        result_list = result_list.reverse()

    # return the merged list
    #debug/verbose: print(f"Merged lists: {input_half1} & {input_half2}\n=> {result_list}\n---")
    return result_list, comparison_counter