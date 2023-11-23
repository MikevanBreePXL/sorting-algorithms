# checkListSort
# returns True if the given list is sorted in a descending order
# returns False if not
def checkListSort(list):
    j = 0
    for i in range(1, len(list)):
        if list[i] > list[j]:
            return False
        j += 1
    return True