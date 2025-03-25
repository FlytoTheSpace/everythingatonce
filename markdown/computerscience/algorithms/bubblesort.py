
sampleList = [5, 4, 2, 6, 7, 2, 3, 1, 9]

def bubbleSort(List):
    loopList = List
    loopListlen = len(loopList)
    while True:
        continues = 0 # Check if all the elements are in order
        for i in range(1, loopListlen):

            j = i - 1
            if j < 0 : continue

            # Switch Elements if left one is bigger
            if loopList[j] > loopList[i]:
                tempElement = loopList[i]
                loopList[i] = loopList[j]
                loopList[j] = tempElement
            else:
                # Increment order if in order
                continues = continues + 1

        if(continues >= (loopListlen - 1)): break # Stop Looping if Sorted
        
    return loopList

print(bubbleSort(sampleList)) # [1, 2, 2, 3, 4, 5, 6, 7, 9]