import random

print("🎉 Welcome to the Student Fun Survey Application 🎉" , 123)

if bool(0) == True:
    print("************")

students = {}

# Collecting Students information
for i in range(3):
    print(f"\n🎓 Student {i + 1} Info")
    name = input("Enter the name of student: ").strip()
    fav_subject = input("Favorite subject: ").strip()
    fun_fact = input("Fun or weird fact about yourself: ").strip()
    snack = input("Snack you'll bring to the party: ").strip()
    mood = input("Mood of the day (Optional): ").strip()

    students[name] = {
        "subject": fav_subject,
        "fact": fun_fact,
        "snack": snack,
        "mood": mood
    }

# View a specific student's information
print("\n🔍 View Student Info")
search_name = input("Enter a student's name to view their details: ").strip()
if search_name in students:
    student = students[search_name]
    print("\n🎉 Information for " + search_name + ":")
    print("📚 Favorite Subject: " + student['subject'])
    print("😄 Fun Fact: "+student['fact'])
    print("🍿 Snack: " + student['snack'])
    print("🧠 Mood: " + student['mood'])
else:
    print("❌ Student not found.")

# Snacks that each student will bring to the party
print("\n🍭 Snacks for the party: ")
for name, details in students.items():
    print(name + " is bringing: "+ details['snack'])

# Vote for the best snack
print("\n🗳️ Vote for the best snack!")
voted_snack = input("Enter the name of your favorite snack: ").strip()

found = False
for name, details in students.items():
    if details['snack'].lower() == voted_snack.lower():
        print("✅ " + name + " brought " + voted_snack +"!")
        found = True

if not found:
    print("😅 Nobody brought that snack, but nice choice!")


winner = random.choice(list(students.items()))
print("\n🏆 Silliest Fun Fact Award goes to...")
print(f"{winner[0]}: \"{winner[1]['fact']}\" 😂")

print("\n🎊 Thanks for participating in the survey!")
