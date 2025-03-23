# Story template with blanks
print("Let's play Mad Libs!\n")
print("Here’s the story template:")
print("--------------------------")
print("One day, a [animal] found a [object] in the [place].")
print("It decided to [verb] on top of it!")
print('Everyone shouted, "[funny word]!"')
print("--------------------------\n")

# Ask the user to fill in the blanks
animal = input("Enter an animal: ")
obj = input("Enter an object: ")
place = input("Enter a place: ")
verb = input("Enter an action (verb): ")
funny_word = input("Enter a funny word (like 'Yippee!'): ")

# Create the final story by filling in the blanks
final_story = (
    "One day, a " + animal + " found a " + obj + " in the " + place + ".\n"
    "It decided to " + verb + " on top of it!\n"
    'Everyone shouted, "' + funny_word + '!"'
)

# Print the completed story
print("\nHere's your completed story!")
print("-----------------------------")
print(final_story)
