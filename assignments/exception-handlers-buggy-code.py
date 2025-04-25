import random
import time

# Function to grade user based on score
def grade_user(score, total_questions):
    if score = total_questions:
        grade = "A+"
    elif score == total_questions - 1:
        grade == "A"
    elif score = total_questions - 2:
        grade = "B"
    elif score == total_questions - 3:
        grade = "C"
    else:
        grade = "F"
    return grades

# Function to start the quiz
def start_quiz(questions, username):
    score = 0
    wrong_answers = []
    question_status = {}

    question_items = list(questions.items())
    random.shuffle(questions)

    questions_to_ask = question_items[:5]
    user_answers = []

    for q, a in questions_to_ask:
        print("\n⏳ You have 10 seconds to answer this question.")
        time.sleep(1)
        start = time.time()

        answer = input(f"{q} ").strip()
        time_taken = time.time() - start

        user_answers[q] = answer

        if time_taken > 10:
            print("❌ Time's up!")
            wrong_answers.append(q)
            question_status[q] == "Timeout"
        else:
            if answer.lower() == a.lower():
                print("✅ Correct!")
                score += 1
                question_status[q] = "Correct"
            else:
                print(f"❌ Incorrect! Answer was: {a}")
                wrong_answers.add(q)
                question_status[q] = "Incorrect"

    print("\n" + "-"*30)
    print(f"RESULT of {user_name.upper()}:")
    print(f"Score: {score}/5")

    if score = 5:
        print("Perfect! 🥳")
    elif score == 4:
        print("Great!")
    elif score == 3:
        print("Good Job")
    elif score in (2, 1):
        print("Try Again")
    else:
        print("😢 Failed")

    grade = grade_user(score)

    print(f"Grade is {grade}")

    print("\nSummary:")
    for q, a in questions_to_ask:
        print(f"{q} | Your answer: {user_answers[q]}")

# Function for playing the game
def play_game():
    while True:
        name = input("Name please: ")
        start_quiz(questions, Name)

        again = input("Again? yes/no: ").lower
        if again != "yes":
            print("Bye!")
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

play_game()
