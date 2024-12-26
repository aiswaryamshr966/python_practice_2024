#This is a manual approach
def findMinimumAndMaximum(numbers):
    if not numbers: raise ValueError("List is Empty")

    #initialize the minimum and maximum to the first element
    min_value = numbers[0]
    max_value = numbers[0]

    #Iterate through the list starting the second element
    for number in numbers[1:]:
        if number < min_value: min_value = number
        if number > max_value: max_value = number

    return min_value, max_value

def findMinimumAndMaximum2(numbers):
    return min(numbers), max(numbers)

#Example Usage
numbers = [1,2,3,4,5,6,7,8,9,10]
min_value, max_value = findMinimumAndMaximum(numbers)
print("Minimum Value: ", min_value, "Maximum Value: ", max_value)