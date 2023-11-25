import time
from check_list_sorted import checkListSort
# insertion sort

def insertion_sort(given_list):
    insertion_list = [given_list[0]]        # take the first element as first result item
    comparison_counter = 0                   # used to count the amount of comparisons taken

    # go through the list for all other values
    for originalIndex in range(1, len(given_list)):
        triggered = False   # variable for if the current element needs to be last
        
        # compare with elements in the result list
        for insertionIndex in range(len(insertion_list)):
            # insert it in place (right before the first lower value found => descending order sort)
            if given_list[originalIndex] > insertion_list[insertionIndex]:
                insertion_list.insert(insertionIndex, given_list[originalIndex])
                triggered = True
                break
            comparison_counter += 1

        # if element hasn't been put in at the end: put it last
        if triggered == False:
            insertion_list.append(given_list[originalIndex])

    # end of for loop of original list means the list is sorted
    # returns the list AND a number for the amount of comparisons spent
    return insertion_list, comparison_counter