import os
import sys

def print_tree(directory, prefix=""):
    try:
        entries = os.listdir(directory)
    except PermissionError:
        print(f"{prefix}|-- [Permission Denied]")
        return
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return

    entries.sort()
    for index, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        connector = "└── " if index == len(entries) - 1 else "├── "
        print(f"{prefix}{connector}{entry}")
        if os.path.isdir(path):
            extension = "    " if index == len(entries) - 1 else "│   "
            print_tree(path, prefix + extension)

if len(sys.argv) != 2:
    print("Usage: python tree_view.py <directory_path>")
    sys.exit(1)

user_input_path = sys.argv[1]
directory = os.path.expanduser(user_input_path)

if not os.path.isdir(directory):
    print("The path provided is not a valid directory.")
    sys.exit(1)

print(f"📁 Tree of: {directory}\n")
print_tree(directory)
