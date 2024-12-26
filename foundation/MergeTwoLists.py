#Merging Two List Manually
def mergeTwoLists(l1, l2):
    finalListLength = len(l1) + len(l2)
    if finalListLength <= 1: raise ValueError("Lists are empty")

    mergedList = []
    i, j = 0, 0

    #Traverse Both The Lists And Append Th Smallest Element To mergedList
    while i<len(l1) and j<len(l2):
        if l1[i] <= l2[j]:
            mergedList.append(l1[i])
            i += 1
        else:
            mergedList.append(l2[j])
            j += 1

    #Append remaining elements of l1
    while i<len(l1):
        mergedList.append(l1[i])
        i += 1

    #Append remaining elements of l2
    while j<len(l2):
        mergedList.append(l2[j])
        j += 1

    return mergedList

#Example Usage
l1 = [1,3,5,7]
l2 = [2,4,6,8]
print(mergeTwoLists(l1, l2))

