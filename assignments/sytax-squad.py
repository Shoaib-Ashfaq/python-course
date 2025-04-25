numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print("Numbers:", numbers[5])

my_tuple = (10, 20, 30)
my_list = list(my_tuple)
my_list[1] = 25
my_tuple = tuple(my_list)

x = 10
if x == 5:
    print("x is 5")
else:
    print("x is not 5")

for i in range(5):
    print(i)

squares = [i*i for i in range(5) if i % 2 == 0]
print("Even squares:", squares)

my_dict = {'a': 3, 'b': 2}
print(my_dict.get('c', 'Key not found'))
my_set = set()
my_set.add((1, 2, 3))
print("Set:", my_set)

count = 0
while count < 5:
    print("Counting...", count)
    count += 1
