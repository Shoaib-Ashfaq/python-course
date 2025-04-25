def check_status(a, b, flag):
    # input constraints
    if not (-10 <= a <= 10 and -10 <= b <= 10):
        return "Error: a and b must be between -10 and 10"
    if flag:
        return a < 0 and b < 0
    else:
        return (a >= 0) != (b >= 0)


a = int(input("Enter first value between -10 and 10: "))
b = int(input("Enter second value between -10 and 10: "))

flag_input = input("Enter Flag (True/False): ").strip().lower()
if flag_input == "true":
    flag = True
elif flag_input == "false":
    flag = False
else:
    print("Invalid flag input! Please enter True or False.")
    exit()

print("Result:", check_status(a, b, flag))
