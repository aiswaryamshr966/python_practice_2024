#This method counts the character in a string
def characterCount(string):
    #Initialize an empty dictionary for storing character count
    characterCount = {}

    #Iterate through each character of the string
    for character in string:
        if character in characterCount:
            characterCount[character] += 1
        else:
            characterCount[character] = 1

    return characterCount


#This method uses built-in method from collections
def characterCountBuiltIn(string):
    from collections import Counter
    return Counter(string)


#Example Usage
string = "Aiswarya Mishra"
print(characterCount(string))
print(characterCountBuiltIn(string))
