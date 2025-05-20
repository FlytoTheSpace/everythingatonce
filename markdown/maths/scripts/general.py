import math

def removeCommon(list1: list[int], list2: list[int])->list[int]:
    removedItems: list = []
    i: int = 0
    while i < len(list1):
        if i >= len(list1): break
        j: int = 0
        while j < len(list2):
            if j >= len(list2): break

            item1 = list1[i]
            item2 = list2[j]

            if (-item1) == item2:
                if item1 < item2:
                    list1[i] = -1
                    list2.pop(j)
                    j = 0
                    continue
                else:
                    list2[j] = -1
                    list1.pop(i)
                    i -= 1
                    j = 0
                    continue

            if item1 == item2:
                removedItems.append(item1)
                list1.pop(i)
                list2.pop(j)
                i -= 1
                break

            j += 1
        i += 1

    return removedItems