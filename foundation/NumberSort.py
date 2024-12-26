#Using Quick Sort Manually For Sorting The Array
#Built In Function Being numbers.sort()
def quickSort(numbers):
    def partition(low, high):
        pivot = numbers[high]
        i=low-1
        for j in range(low, high):
            if numbers[j] < pivot:
                i+=1
                numbers[i], numbers[j] = numbers[j], numbers[i]
        numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
        return i+1

    def quickSortRecursive(low, high):
        if low < high:
            pivot = partition(low, high)
            quickSortRecursive(low, pivot - 1)
            quickSortRecursive(pivot + 1, high)

    quickSortRecursive(0, len(numbers) - 1)
    return numbers

#Example Usage
numbers = [4,1,7,4,9,3,6,8]
print("Original Unsorted Array:", numbers)
print("Sorted Array:", quickSort(numbers))