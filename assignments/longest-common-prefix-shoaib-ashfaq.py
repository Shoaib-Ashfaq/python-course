def longest_common_prefix(strs):
    if not (1 <= len(strs) <= 200):
        return "Error: Length of List must be between 1 and 200."

    for s in strs:
        if not (0 <= len(s) <= 200):
            return "Error: Each string must be between 0 and 200 characters."

        if s != "" and not s.islower():
            return "Error: Strings must contain only lowercase letters."

    prefix = strs[0]

    for string in strs[1:]:
        while not string.startswith(prefix):

            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

strs1= ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]

print(longest_common_prefix(strs2))
print(longest_common_prefix(strs1))
