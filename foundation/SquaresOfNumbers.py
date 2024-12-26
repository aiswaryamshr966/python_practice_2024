def squaresAdvancedLoop(numbers):
    numbers = [x**2 for x in numbers]
    return numbers;

def squaresLoop(numbers):
    length = len(numbers)
    for i in range(0,length):
        numbers[i] = numbers[i]**2
    return numbers;

print("Finding Square Of Each Number in the list using advanced loop:",squaresAdvancedLoop([1,2,3,4,5]))
print("Finding Square Of Each Number in the list using normal loop",squaresLoop([7,4,2,6,4]))