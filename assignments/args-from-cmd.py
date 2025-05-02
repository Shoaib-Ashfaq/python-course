import sys

print("All arguments:", sys.argv)
print("File name:", sys.argv[0])

if len(sys.argv) > 1:
    print("Hello", end=" ")
    for i in range(1, len(sys.argv)):
        print(sys.argv[i], end=" ")
    print("")
else:
    print("No arguments given.")
