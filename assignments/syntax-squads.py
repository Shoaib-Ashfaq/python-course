numbers = [1, 2, 3, 4, 5]
numbers.append(6) # Typo: 'apend' instead of 'append'
print("Numbers:", numbers[5])

my_tuple = (10, 20, 30)
# fix TypeError
my_list = list(my_tuple)
my_list[1] = 25
my_tuple = tuple(my_list)

x = 10
if x == 5: # SyntaxError: should be '=='
    print("x is 5")
else:
    print("x is not 5")

for i in range(5): # add colon
    print(i)  # Indentation Error and missing colon

squares = [i*i for i in range(5) if i % 2 == 0]  # SyntaxError in condition ==
print("Even squares:", squares)

my_dict = {'a': 3, 'b': 2}
print(my_dict.get('c', 'Key not found')) # KeyError: 'c' doesn't exist

my_set = set()
my_set.add((1, 2, 3)) # TypeError: list is unhashable
print("Set:", my_set)

count = 0
while count < 5:
    print("Counting...", count)
    count += 1  # add increment, to avoid infinite loop



# output
# Numbers: 6
# x is not 5
# 0
# 1
# 2
# 3
# 4
# Even squares: [0, 4, 16]
# Key not found
# Set: {(1, 2, 3)}
# Counting... 0
# Counting... 1
# Counting... 2
# Counting... 3
# Counting... 4
