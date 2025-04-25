import time

# def my_len(a):
#     count = 0
#     for a in a:
#         count += 1
#     return count

# str1 = [1,2,3,4]
# print(my_len(str1))


# my_string = "Hello world"


# def my_sum(a,b,c):
#     return a+b+c

# print(my_sum(4,5,7))


# def func(a):
#     return a+2

# user_input = int(input("Enter a number: "))
# print("After adding 2 into your number the number become",func(user_input))


# def func1():
#     print("Function in python")

# func1()

# def three_int_sum(a,b,c):
#     """This function take three arguments values must be int/float and return their sum"""
#     return a+b+c

# print(three_int_sum.__doc__)
# print(three_int_sum(4,5.5,7))

# def func2():
#     str1 = "hello"
#     str2 = "hey"
#     str3 = "How are you"
#     return [str1, str2, str3]


# rv1,rv2,rv3 = func2()
# rv = func2()
# print(type(rv))
# print(rv)

# def two_num_sum(a,b):
#     """This function take two arguments, values must be int/float and return their sum
#         Arguments:
#             a - first number
#             b - second number
#     """
#     return a+b

# print(two_num_sum.__doc__)
# print(two_num_sum(4,5.5))

# def sum_of_square_of_a_list(a):
#     return sum([i**2 for i in a])


# print(sum_of_square_of_a_list([1,2,3]))



# def list_of_odd_numbers(a):
#     return [i for i in a if i%2 != 0]

# print("List of odd numbers are: ", list_of_odd_numbers([1,2,3,4,5,6,7,8,9]))


# def check_bool():
#     n = int(input("Enter a number: "))
#     return n%2 == 0

# if check_bool():
#     print("Entered Number is Even")
# else:
#     print("Entered Number is odd")


# def func1(t1):
#     t1 = 'x'
# my_tup = (1,2,3)

# print("Before", my_tup)
# print("After", func1(my_tup))


# def myfunc(x, y, z):
#     x = x + 1
#     y = y + "1"
#     z[0] = z[0] + 5
#     return x, y, z


# a = 10
# b = "20"
# c = [30,4,7]
# myfunc(a,b ,c)
# print(a,b,c)

# def display(name= "Shoaib Ashfaq", age = 27):
#     print("Name :", name, ", Age: ", age )

# display(age=9)

# def mysub(a,b):
#     return a-b

# print(mysub(b=3, a=8))


# def countdown(seconds):
#     while seconds > 0:
#         mins, secs = divmod(seconds, 60)
#         timer = f'{mins:02d}:{secs:02d}'
#         print(timer)
#         time.sleep(1)
#         seconds -= 1
#     print("Time's up!")


# n = int(input("Enter a number: "))
# countdown(n)


def chatbot():
    qa_dict = {
        "hello": "Hi! how are you",
        "what is your name": "I am a simple chatbot!",
        "how are you": "I'm doing well, thank you! for asking",
        "what is python": "Python is a powerful, easy-to-learn programming language.",
        "who created python": "Python was created by Guido van Rossum.",
        "what is the capital of pakistan": "Islamabad",
        "what is ai": "AI stands for Artificial Intelligence.",
        "bye": "Goodbye! Have a nice day!"
    }

    print(" Ask me anything (type 'bye' to exit):\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "bye":
            print("Bot: Goodbye! 👋")
            break
        elif user_input in qa_dict:
            print("Bot:", qa_dict[user_input])
        else:
            print("Bot: Sorry, I don't understand that question.")

chatbot()
