# Question: Check if a String Contain Digit (NOT  USING ISDIGIT METHOD)
simpleString = "abc123"
print("0" in simpleString or "1" in simpleString or "2" in simpleString or "3" in simpleString or "4" in simpleString or "5" in simpleString or "6" in simpleString or "7" in simpleString or "8" in simpleString or "9" in simpleString)
# print(any(char in "0123456789" for char in simpleString))

# Question: Check if a String start with Vowel
print("a" in simpleString[0] or "e" in simpleString[0] or "i" in simpleString[0] or "o" in simpleString[0] or "u" in simpleString[0])
print(simpleString.startswith("a") or simpleString.startswith("e") or simpleString.startswith("i")  or simpleString.startswith("o") or simpleString.startswith("u"))


print(simpleString.en)
# Question: Check if a String End with a specific Character
specificChar = "#"
print(simpleString.endswith(specificChar))

# Question: Check if a String Contain Any special char (@, #,  $, % & *)
print("@" in simpleString or "#" in simpleString or "$" in simpleString or "%" in simpleString or "&" in simpleString or "*" in simpleString)

# Question: Check if a Number is present as a substring
numberToFind = 123
print(str(numberToFind) in simpleString)


# Question: Check if a String contain both numbers and alphabets
print(simpleString.isalnum())

# If a specific word exist in a sentence
simpleSentence = "My name is shoaib"
wordToCheck = "Shoaib"
print(wordToCheck.lower() in simpleSentence.lower())

# Check if the string has vowel
print("a" in simpleString or "e" in simpleString or "i" in simpleString or "o" in simpleString or "u" in simpleString)

# String is palindrome or not
palindromeStr = "Madam"
print(palindromeStr.lower() == palindromeStr.lower()[::-1])
