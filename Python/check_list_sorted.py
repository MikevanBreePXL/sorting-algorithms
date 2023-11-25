# checkListSort
# returns True if the given list is sorted in a descending order
# returns False if not
def checkListSort(list, direction = "ascending"):
    j = 0
    match direction:
        case "ascending":
            for i in range(1, len(list)):
                if list[i] < list[j]:
                    return False
                j += 1
            return True
        case "descending":
            for i in range(1, len(list)):
                if list[i] > list[j]:
                    return False
                j += 1
            return True
        case _:
            error = ValueError
            error.add_note('direction needs to be default, "ascending" or "descending"')