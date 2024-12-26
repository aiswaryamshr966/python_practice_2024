string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for letter in string:
    if letter in vowels: count = count+1

print("Number of vowels:", count)