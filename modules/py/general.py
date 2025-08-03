
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


def removeCommon2(array: list[list[int]])->list[list[int]]:
    """
    given a matrix of arrays, removes any common number between them

    $O(n^2)$ is the space-time complexity even though it has 4 nested loops, but since the input grows Quadratically and not Linearly

    eg.

    ```py
    
    removeCommon2([
        [2, 4, 2],
        [10, 4, 2, 5],
        [2, 5, 20, 7]
    ])
    # ->
    # [
    #     [],
    #     [10],
    #     [20, 7]
    # ]
    ```
    """
    listCount = len(array)
    for Lindex in range(listCount):
        i: int = 0
        while i < len(array[Lindex]):
            num1: int = array[Lindex][i]
            matchFound: bool = False
            Lindex2 = Lindex + 1
            while Lindex2 < listCount:
                if (matchFound): break
                j: int = 0
                while j < len(array[Lindex2]):
                    num2: int = array[Lindex2][j]
                    if (num1 == num2):
                        array[Lindex].pop(i)
                        array[Lindex2].pop(j)
                        i -= 1
                        matchFound = True
                    if (matchFound): break
                    j += 1
                Lindex2 += 1
            i += 1
    return array
