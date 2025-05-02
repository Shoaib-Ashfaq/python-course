roman_numeral = input("Enter a Roman numeral: ").strip()

if not (1 <= len(roman_numeral) <= 15):
    print("Roman numeral length must be between 1 and 15 characters.")
    exit()

valid_chars = "IVXLCDM"
for s in roman_numeral:
    if s.upper() not in valid_chars:
        print("Roman numeral contains invalid characters.")
        exit()


roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


total = 0
prev_value = 0

for char in reversed(roman_numeral.upper()):
    value = roman_values[char]

    if value < prev_value:
        total -= value
    else:
        total += value

    prev_value = value

if not (1 <= total <= 3999):
    print("Roman numeral must represent a number between 1 and 3999.")
    exit()


print(f"The integer value of {roman_numeral} is {total}.")
