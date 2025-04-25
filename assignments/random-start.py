import random

groups = [
    "The Exception Handlers",
    "Syntax Squads",
    "Python Stars",
    "Debugger"
]

random.shuffle(groups)

print("📢 Presentation Order:")
print(f"1️⃣ First:   {groups[0]}")
print(f"2️⃣ Second:  {groups[1]}")
print(f"3️⃣ Third:   {groups[2]}")
print(f"4️⃣ Fourth:  {groups[3]}")
