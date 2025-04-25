import random
import time

# Function to grade user based on score
def grade_user(score, total_questions):
    if score == total_questions:
        grade = "A+"
    elif score == total_questions - 1:
        grade = "A"
    elif score == total_questions - 2:
        grade = "B"
    elif score == total_questions - 3:
        grade = "C"
    else:
        grade = "F"
    return grade

# Function to start the quiz
def start_quiz(questions, user_name):
    score = 0
    wrong_answers = []
    question_status = {}

    # Shuffling questions
    question_items = list(questions.items())
    random.shuffle(question_items)

    # Ask 5 random questions
    questions_to_ask = question_items[:5]

    user_answers = {}

    for question, correct_answer in questions_to_ask:
        print("\n⏳ You have 10 seconds to answer this question.")
        time.sleep(1)
        start_time = time.time()

        answer = input(f"{question} ").strip()
        elapsed_time = time.time() - start_time

        user_answers[question] = answer

        if elapsed_time > 10:
            print("❌ Time's up! You didn't answer in time.")
            wrong_answers.append(question)
            question_status[question] = "Incorrect (Timeout)"
        else:
            if answer.lower() == correct_answer.lower():
                print("✅ Correct!")
                score += 1
                question_status[question] = "Correct"
            else:
                print(f"❌ Incorrect! The correct answer was: {correct_answer}")
                wrong_answers.append(question)
                question_status[question] = "Incorrect"

    # Show final score and grade
    print("\n" + "="*50)
    print(f"\n🎓 RESULT SUMMARY for {user_name.upper()}:\n")
    print(f"📊 Final Score: {score} out of 5")

    # Excitement or Encouragement messages
    if score == 5:
        print("🎉 HURRAY!! You nailed it! Perfect score! 🥳🔥")
    elif score == 4:
        print("👏 Great job! Just missed one. You're so close! 💯")
    elif score == 3:
        print("👍 Good effort! You're halfway there! Keep going! 🚀")
    elif score == 2:
        print("🙂 Not bad! Try again to improve your score! 🔁")
    elif score <= 1:
        print("😢 Ahhh! Better luck next time. Don't give up! 💪 Try again?")

    grade = grade_user(score, 5)
    print(f"🏅 Grade: {grade}")
    print("\n" + "="*50)

    # Detailed answer breakdown
    print("\n📋 Question/Answer Summary:")
    for question, correct_answer in questions_to_ask:
        user_response = user_answers[question]
        status = question_status[question]
        emoji = "✅" if status == "Correct" else "❌"
        print(f"\nQ: {question}\nYour Answer: {user_response}\nCorrect Answer: {correct_answer} {emoji}")


# Function for playing the game
def play_game():
    while True:
        name = input("Please enter your name: ").strip()
        print(f"\n👋 Welcome to the Quiz Master, {name}!\n")
        start_quiz(questions, name)

        play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("👋 Thank you for playing! Goodbye!")
            break


questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the smallest prime number?": "2",
    "In which year did the Titanic sink?": "1912",
    "What is the chemical symbol for water?": "H2O",
    "What is the currency of Japan?": "Yen",
    "What is the capital of Pakistan?": "Islamabad",
    "Who is the founder of Pakistan?": "Muhammad Ali Jinnah",
    "What is the national language of Pakistan?": "Urdu",
    "What is the national sport of Pakistan?": "Hockey",
    "Which river is the longest in Pakistan?": "Indus",
    "Which city is known as the heart of Pakistan?": "Lahore",
    "In which year did Pakistan gain independence?": "1947",
    "Who was the first Prime Minister of Pakistan?": "Liaquat Ali Khan",
    "Which mountain is the highest in Pakistan?": "K2",
    "What does the white color in Pakistan's flag represent?": "Minorities",
}

# Starting the game
play_game()
