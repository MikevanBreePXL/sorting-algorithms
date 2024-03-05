from shuffle_list import shuffle_fischer_yates

def bogo_sort(unsorted_list, sort_order):
    if sort_order.lower()[0:4] != "desc" and sort_order.lower()[0:3] != "asc":
        raise Exception('direction should be default, "asc(ending)" or "desc(ending)", your value: ' + sort_order)
     
    comparison_amount = 0
    while True:
        if sort_order == "desc":
            unsorted_list.reverse()

        sorted_trigger = True
        for i in range(1, len(unsorted_list)):
            comparison_amount += 1
            if unsorted_list[i] < unsorted_list[i-1]:
                sorted_trigger = False
                unsorted_list = shuffle_fischer_yates(unsorted_list)

        if sorted_trigger == True:
            return unsorted_list, comparison_amount
