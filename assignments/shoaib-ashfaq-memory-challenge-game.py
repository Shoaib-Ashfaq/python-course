import random
import time
import os

items = ['apple', 'banana', 'cat', 'dog', 'elephant', 'flower', 'guitar', 'hat', 'ice', 'jacket']

# To clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# To generate random events
def random_event():
    events = ["🎉 Surprise! You get 2 extra seconds!", "⚡ A trap! You lose 2 seconds!", "🎁 Bonus! You get an extra point!"]
    return random.choice(events)

# game logic
def play_memory_game():
    while True:
        memory_list = []
        score = 0
        round_number = 1
        time_to_memorize = 3

        # Creating a list to store round details (round_number, memory_list, user_input)
        round_details = []

        print("🧠 Welcome to the Memory Challenge Game!")
        print("You will see a list of items for a few seconds.\nTry to remember them in order!\n")

        while True:
            print(f"\n🔁 Round {round_number}")
            new_item = random.choice(items)
            memory_list.append(new_item)

            # Add random event
            event = random_event()
            print("*"*50)
            print(event)
            print("*"*50)

            # Apply the random event effects
            if event == "🎉 Surprise! You get 2 extra seconds!":
                time_to_memorize += 2
            elif event == "⚡ A trap! You lose 2 seconds!":
                time_to_memorize = max(1, time_to_memorize - 2)  # Ensure time does not become negative
            elif event == "🎁 Bonus! You get an extra point!":
                score += 1

            print(f"🔍 Memorize this sequence (you have {time_to_memorize} seconds):")
            print(memory_list)
            time.sleep(time_to_memorize)
            clear_screen()

            print("❓ Now enter the items you remember, in the correct order!")
            user_input = []
            for i in range(len(memory_list)):
                word = input(f"Item {i + 1}: ").strip().lower()
                user_input.append(word)

            # Using list comprehension to check if user input matches memory list
            correct_input = [memory_list[i] == user_input[i] for i in range(len(memory_list))]
            if all(correct_input):
                print("✅ Correct! You're awesome!")
                score += 1
                round_number += 1
            else:
                print("❌ Oops! That's not quite right.")
                print(f"The correct sequence was: {memory_list}")
                print(f"You entered: {user_input}")
                print(f"\n🏁 Game Over! You reached round {round_number - 1}")
                print(f"🎯 Final Score: {score}")
                round_details.append([round_number, memory_list.copy(), user_input])
                break

            round_details.append([round_number - 1, memory_list.copy(), user_input])


        # Print round details after the game ends
        print("\n🏆 Round Details:")
        for round_info in round_details:
            print(f"Round {round_info[0]}:")
            print(f"  Memory List: {round_info[1]}")
            print(f"  Your Input: {round_info[2]}")
            print("-" * 30)

        # Ask if player wants to restart
        play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("👋 Thanks for playing! Goodbye!")
            break
        clear_screen()

# Start the game
play_memory_game()
