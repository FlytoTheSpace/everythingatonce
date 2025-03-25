
sampleList = [5, 4, 2, 6, 7, 2, 3, 1, 9]

def insertionsort(List):
    loopList = List
    loopListlen = len(loopList)

    for i in range(1, loopListlen):
        element = loopList[i] # Selected Element

        for j in range(i):
            # Adjacent Elements
            Pelement = loopList[j]
            Nelement = loopList[j + 1]
            
            # Insert if previous is greater than current
            if Pelement >= element:
                loopList.pop(i)
                loopList.insert(j, element)
                break

            # Insert Element if it fits in between the 2 elements
            if (Pelement <= element) and (element <= Nelement):
                loopList.pop(i)
                loopList.insert(j + 1, element)
                break

    return loopList

print(insertionsort(sampleList)) # [1, 2, 2, 3, 4, 5, 6, 7, 9]