simpleString = input("Enter a simple string: ")
print("\n\n")

# Question: Check if a String Contain Digit (NOT  USING ISDIGIT METHOD)
print("Is Digit Present in simple string? " , ("0" in simpleString or "1" in simpleString or "2" in simpleString or "3" in simpleString or "4" in simpleString or "5" in simpleString or "6" in simpleString or "7" in simpleString or "8" in simpleString or "9" in simpleString))
print("\n\n")

# Question: Check if a String start with Vowel
print("Is String starts with a vowel " ,("a" in simpleString[0] or "e" in simpleString[0] or "i" in simpleString[0] or "o" in simpleString[0] or "u" in simpleString[0]))
print("\n\n")

# print( "Is String starts with a vowel " , (simpleString.startswith("a") or simpleString.startswith("e") or simpleString.startswith("i")  or simpleString.startswith("o") or simpleString.startswith("u")))
# print("\n\n")


# Question: Check if a String End with a specific Character
specificChar = input("Enter a specific character: ")
print("\n\n")
print("Is String end with "+ specificChar + ", " , simpleString.endswith(specificChar))
print("\n\n")

# Question: Check if a String Contain Any special char (@, #,  $, % & *)
print("Is String contain any special character like (@, #,  $, % & *) " , ("@" in simpleString or "#" in simpleString or "$" in simpleString or "%" in simpleString or "&" in simpleString or "*" in simpleString))
print("\n\n")

# Question: Check if a Number is present as a substring
numberToFind = input("Enter a number: ")
print("\n\n")
print("Is " + numberToFind + " present as a substring ? " , numberToFind in simpleString)
print("\n\n")


# Question: Check if a String contain both numbers and alphabets
print("Is simple String contain both numbers and alphabets? ", simpleString.isalnum() and not simpleString.isalpha() and not simpleString.isalpha())
print("\n\n")

# If a specific word exist in a sentence
simpleSentence = input("Enter a simple sentence: ")
print("\n\n")
wordToCheck = input("Enter word to check in the sentence: ")
print("\n\n")

print("Is word " + wordToCheck +" Present is the sentence? " , wordToCheck.lower() in simpleSentence.lower())
print("\n\n")

# Check if the string has vowel
print("Is simple String contain vowel? ", ("a" in simpleString or "e" in simpleString or "i" in simpleString or "o" in simpleString or "u" in simpleString))
print("\n\n")

# String is palindrome or not
palindromeStr = input("Enter a string to check if it's palindrome or not: ")
print("\n\n")

print("Is simple String palindrome? ", palindromeStr.lower() == palindromeStr.lower()[::-1])
print("\n\n")

print("Arithmetic Operators are: \n \t 1: Addition , Symbol + \n \t 2: Subtraction , Symbol - \n \t 1: Multiplication , Symbol *")
