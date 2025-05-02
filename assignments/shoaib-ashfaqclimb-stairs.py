def climb_stairs(n):
    if n<2:
        return 1

    return climb_stairs(n - 1) + climb_stairs(n - 2)

try:
    user_input = input("Enter the number of steps (1 to 45): ")
    n = int(user_input)

    if n < 1 or n > 45:
        raise ValueError("Number must be between 1 and 45.")

    result = climb_stairs(n)
    print(f"\nThere are {result} distinct ways to climb {n} steps.")

except ValueError as e:
    print(f"Invalid input: {e}")
