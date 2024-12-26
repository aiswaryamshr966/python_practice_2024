def duplicateRemovalBuiltin(numbers):
    return list(set(numbers))

def duplicateRemovalManual(numbers):
    numberSet = []
    for number in numbers:
        if number not in numberSet:
            numberSet.append(number)

    numberSet.sort()
    return numberSet

numbers = [1,2,6,2,7,9,3,1,0,3,4,5,6,7,8,9,10]
print("Original List:",numbers)

#This removes the duplicates based on built in functions to convert list into set
#This built in Function also sorts the set
print("After Duplicate Removal:",duplicateRemovalBuiltin(numbers))

#This manually checks the list and removes the duplicates
#This manual apprach doesn't sort the set
print("After Manual Duplicate Removal:",duplicateRemovalManual(numbers))
