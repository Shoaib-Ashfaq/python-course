identity = [
    "loves biryani",
    "name: Hammad",
    "pet rock",
    "hobby: traveling and caligraphy",
    "plays badminton",
    "remembers being a toaster"
]

# 1. Change name
identity[identity.index("name: Hammad")] = "name: Shoaib"  # Replace with your actual name

# 2. Replace "remembers being a toaster"
identity[identity.index("remembers being a toaster")] = "remembers being a Python programmer"

# 3. Remove "pet rock"
identity.remove("pet rock")

# 4. Update food item
identity[identity.index("loves biryani")] = "loves nihari"

# 5. Replace hobby
identity[identity.index("hobby: traveling and caligraphy")] = "hobby: Outdoor gaming"  # Replace with your real hobby

# 6. Append the human trait
identity.append("drinks water like a normal human")

# 7. Reverse the list
identity = identity[::-1]

# 8. Print new identity
print(identity)


var1 = 1
var2 = 3
var3 = "The sum is "
print(var3, var1+var2)
