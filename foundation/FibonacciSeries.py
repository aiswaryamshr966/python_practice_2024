number = int(input("Enter the number of terms: "))
a, b = 0, 1

fib_sequience = []

for _ in range(number):
    fib_sequience.append(a)
    a, b = b, a + b

print("Fibonacci series: ", fib_sequience)