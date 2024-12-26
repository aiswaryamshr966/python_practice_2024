def sumDigits():
    number = int(input("Enter a number: "))
    sum = 0

    for digit in str(number):
        sum += int(digit)

    print("Sum Of The Digits Of", number, ":", sum)

def sumDigitsBuiltin():
    num = input("Enter a number: ")
    sum_of_digits = sum(int(digit) for digit in num)
    print("Sum of digits of",num,":",sum_of_digits)

sumDigits()
sumDigitsBuiltin()