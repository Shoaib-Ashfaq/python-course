import sys
import random

jokes = {
    'tech': [
        "The future masters of technology will have to be light-hearted and intelligent. The machine easily masters the grim and the dumb.",
        "Why did the computer go to therapy? It had too many bytes of anxiety!"
    ],
    'bird': [
        "What do you call a lost parrot? A polygon",
        "Why do hummingbirds hum? they don’t know the lyrics"
    ],
    'animal': [
        "What do you call a dog magician? A labracadabrador.",
        "What do you call a porcupine interviewing for a job at a balloon factory? Unemployed."
    ]
}

def tell_joke(category, count=1):
    category = category.lower()

    if category not in jokes:
        print(f"🚫 Sorry, '{category}' is not a valid category.")
        print(f"✅ Available categories: {', '.join(jokes.keys())}")
        return

    joke_list = jokes[category]
    available_jokes = len(joke_list)

    if count > available_jokes:
        count = available_jokes

    selected_jokes = random.sample(joke_list, count)

    print("\n😂 Here's your joke(s):\n")
    for i in range(len(selected_jokes)):
        print(f"{i + 1}. {selected_jokes[i]}")


if len(sys.argv) < 2:
    print("🚨 Error: You must provide a joke category (tech, animal, bird)!")
    sys.exit()

category = sys.argv[1]

if len(sys.argv) >= 3:
    try:
        count = int(sys.argv[2])
    except ValueError:
        print("🚨 Error: Count must be a number.")
        sys.exit()
else:
    count = 1

tell_joke(category, count)
