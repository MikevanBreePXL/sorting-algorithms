import time
from check_list_sorted import checkListSort
# insertion sort

def insertion_sort(given_list, direction = "ascending"):
    if direction.lower()[0:4] != "desc" and direction.lower()[0:3] != "asc":
        raise Exception('direction needs to be default, "asc(ending)" or "desc(ending)", your value: ' + direction)

    insertion_list = [given_list[0]]        # take the first element as first result item
    comparison_counter = 0                   # used to count the amount of comparisons taken

    # go through the list for all other values
    for given_list_index in range(1, len(given_list)):
        triggered = False   # variable for if the current element needs to be last
        
        # compare with elements in the result list
        for insertion_index in range(len(insertion_list)):
            # insert it in place (right before the first lower value found => descending order sort)
            #debug/verbose: print(f"Compare: [{given_list[given_list_index]}](input element) & [{insertion_list[insertion_index]}](inserted element)")
            if given_list[given_list_index] > insertion_list[insertion_index]:
                #debug/verbose: print(f"Adding [{given_list[given_list_index]}] before [{insertion_list[insertion_index]}]")
                insertion_list.insert(insertion_index, given_list[given_list_index])
                triggered = True
                break
            comparison_counter += 1

        # if element hasn't been put in at the end: put it last
        if triggered == False:
            #debug/verbose: print(f"Adding [{given_list[given_list_index]}] to the end")
            insertion_list.append(given_list[given_list_index])

    # end of for loop of original list means the list is sorted

    if direction.lower()[0:4] == "desc":
        insertion_list = insertion_list.reverse()

    # returns the list AND a number for the amount of comparisons spent
    return insertion_list, comparison_counter