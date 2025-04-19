n = int(input("Enter countof fibonacchi numbers you want to print: " ))
i = 1

if i < 1:
    fib = []
elif n == 1:
    fib = [0]
elif n == 2:
    fib = [0, 1]

elif n > 2:
    fib = [0, 1]
    while (i < n-1):
        fib.append(fib[i] + fib[i-1])
        i+=1

print("Required Fibnoccahi Series: ", fib)
