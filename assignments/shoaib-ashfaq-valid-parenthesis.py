matching_brackets = {
    "(": ")",
    "{": "}",
    "[": "]"
}

def is_valid_parentheses(expression):
    i, j = 0, len(expression) - 1
    is_valid = True
    all_keys = list(matching_brackets.keys())
    stack = []

    for e in expression:
        if e in all_keys:
            stack.append(e)
        else:
            if len(stack) == 0 or matching_brackets[stack.pop()] != e:
                is_valid = False
                break

    return is_valid

valid_characters = "(){}[]"
all_keys = list(matching_brackets.keys())

try:
    user_input = input("Enter a combination of brackets to validate: ").strip()

    if not (1 <= len(user_input) <= 10000):
        raise ValueError("Input length must be between 1 and 10,000 characters.")

    for ch in user_input:
        if ch not in valid_characters:
            raise ValueError("Input must contain only bracket characters: (), {}, []")

    if is_valid_parentheses(user_input):
        print("The bracket string is VALID.")
    else:
        print("The bracket string is NOT valid.")

except ValueError as ve:
    print(f"Error: {ve}")
