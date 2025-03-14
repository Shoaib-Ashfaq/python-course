# Input string
text = input("Enter a string to analyze: ")

# Total characters
char_count = len(text)

# Uppercase letters
upper_count = len(list(filter(str.isupper, text)))

# Lowercase letters
lower_count = len(list(filter(str.islower, text)))

# Digits
digit_count = len(list(filter(str.isdigit, text)))

# Words (split by spaces)
word_count = len(text.split())

# Spaces
space_count = text.count(' ')

# Words
words = text.split()
word_count = len(words)

# Title case characters: Count words that start with an uppercase letter
title_case_count = len(list(filter(str.istitle, words)))

# Output
print("Total characters:", char_count)
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
print("Digits:", digit_count)
print("Words:", word_count)
print("Spaces:", space_count)
print("Title case word count:", title_case_count)
