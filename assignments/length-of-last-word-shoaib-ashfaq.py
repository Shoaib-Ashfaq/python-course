sample_string = input("Please enter the string: ").strip()

if not (1 <= len(sample_string) <= 10000):
    print("Error: String length must be between 1 and 10,000")
else:
    if not all(char.isalpha() or char == ' ' for char in sample_string):
        print("Error: String can only contain English letters and spaces.")
    else:
        words_list = sample_string.split()
        if len(words_list) == 0:
            print("Error: The input must contain at least one word.")
        else:
            print("Length of the last word is:", len(words_list[-1]))
