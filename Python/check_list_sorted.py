# checkListSort
# returns True if the given list is sorted in a descending order
# returns False if not
def checkListSort(list, direction = "ascending"):
    j = 0
    match direction[0:3]:
        case "asc":
            for i in range(1, len(list)):
                if list[i] < list[j]:
                    return False
                j += 1
            return True
        case "des":
            for i in range(1, len(list)):
                if list[i] > list[j]:
                    return False
                j += 1
            return True
        case _:
            raise Exception('direction needs to be default, \"asc(ending)\" or \"des(cending)\"')