# 1. Create a list of squares
squares = [x**2 for x in range(1, 11)]
print("list of squares from 1-10 ", squares)
print("\n")

# 2. Extract first letters
fruits = ["apple", "banana", "cherry"]
first_letter = [fruit[0] for fruit in fruits]
print("first letter of all fruits from fruits list ", first_letter)
print("\n")

# 3. Filter out odd numbers
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers", even_numbers)
print("\n")

# 4. Map numbers to their squares
squares_dict = {x: x**2 for x in range(1, 6)}
print("Square numbers", squares_dict)
print("\n")

# 5. Map words to their lengths
map_word_to_length = {fruit: len(fruit) for fruit in fruits}
print("word with its length", map_word_to_length)
print("\n")

# 6. Remove vowels from strings
words = ["hello", "world"]
vowels = "aeiouAEIOU"
without_vowels = [''.join([char for char in word if char not in vowels]) for word in words]
print("Words without vowels", without_vowels)
print("\n")


# 7. Filter dict entries by value
original_dict = {"a": 10, "b": 20, "c": 30}
filtered_dict = {k: v for k, v in original_dict.items() if v > 15}
print("Filtered Values are", filtered_dict)
print("\n")

# 8. Inverting a dictionary
original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {v: k for k, v in original_dict.items()}
print("Original Dictionary", original_dict)
print("Inverted Dictionary", inverted_dict)
print("\n")

# 9. Find palindromes
words = ["madam", "apple", "racecar", "python"]
palindromes = [word for word in words if word == word[::-1]]
print("Palindromes ", palindromes)
print("\n")
