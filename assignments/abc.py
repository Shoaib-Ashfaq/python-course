# import os

# a = input("Enter your name: ");

# os.system(f'python3 args-from-cmd.py {a}')


# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(f"Result: {result}")
#     tup1 = (1,4,5,6,10)
#     tup1[0] = 3
# except ValueError:
#     print(" You must enter a valid number.")
# except ZeroDivisionError:
#     print(" Cannot divide by zero!")
# except Exception as e:
#     print(f" Something went wrong: {e}")

# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
# except ValueError:
#     print("Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Division by zero is not allowed!")
# except Exception as e:
#     print(f"Unexpected error: {e}")
# else:
#     print(f"Success! Result is: {result}")
# finally:
#     print("Program finished. Thanks for using it!")


# try:
#     user_age = int(input("Enter your age for registration: "))
#     if user_age < 0:
#         raise ValueError("Age cannot be negative!")
#     elif user_age < 18:
#         raise ValueError("You must be at least 18 years old to register.")
# except ValueError as ve:
#     print(f"Error: {ve}")
# except Exception as e:
#     print(f"Unexpected error: {e}")
# else:
#     print("Registration successful!")
# finally:
#     print("Process ended.")



# try:
#     user_age = int(input("Enter your age: "))
#     assert user_age >= 0, "Age cannot be negative!"
#     assert user_age >= 18, "You must be at least 18 years old to register."
# except AssertionError as ae:
#     print(f"Assertion Error: {ae}")
# except Exception as e:
#     print(f"Unexpected error: {e}")
# else:
#     print("Registration successful!")
# finally:
#     print("🔔 Process ended.")


import math as m
from math import *

print(dir())

print(m.ceil(2.3))

print(m.factorial(5))
print(floor(5))
print(tau)
print(e)
print(inf)
