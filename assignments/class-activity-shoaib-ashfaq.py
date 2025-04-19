#(1) count vowels
sample_string = input("Please Enter the string: ")
vowels = "aeiouAEIOU"
count = 0

for char in sample_string:
    if char in vowels:
        count += 1

print("Number of vowels in your strings are: ", count)
print("\n\n")

#(2)  Printing of char using for loop
print("Character of a string one by one are")
for char in sample_string:
    print(char)
print("\n\n")

#(3) Even numbers between 1 and 20
print("Even numbers between 1 and 20:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num)
print("\n\n")

#(4) Multiplication Table of 5
print("📊 Multiplication Table of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
print("\n\n")

#(5) Sum of numbers between 1 - 100
count = 1
total = 0
while count <= 100:
    total += count
    count += 1
print("\n\n")


#(6) factorial of a number
num = int(input("Enter a number to find its factorial: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"Factorial of {num} is: {factorial}")
print("\n\n")

#(7) check if a number is prime or not
num = int(input("Enter a number to check if it's prime: "))
if num > 1:
    is_prime = True
    i = 2

    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num, " is a prime number.")
    else:
        print(num, " is not a prime number.")
else:
    print(num, " is not a prime number.")
print("\n\n")


#(8) Numbers divisible by both 3 and 5
print("Numbers divisible by both 3 and 5 between 1 and 100:")
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
print("\n\n")

#(9) check if string is palindrome
text = input("Enter a string to check if it's a palindrome: ").lower()
text = text.strip()

start = 0
end = len(text) - 1
is_palindrome = True

while start < end:
    if text[start] != text[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1

if is_palindrome:
    print(text, " is a palindrome!")
else:
    print(text, " is not a palindrome.")

print("\n\n")

#(10) Generate Pattern
for i in range(1, 6):
    print("*" * i)
print("\n\n")


# Reverse a number
num = int(input("Enter a number to reverse "))
original_num = num
rv = 0
while True:
    if num < 10:
        rv = (rv * 10) +  (num % 10)
        break
    rv = (rv * 10) +  (num % 10)
    num //= 10

print("\n",original_num, "in reverse order is " , rv)
