from datetime import datetime, date

def days_until_birthday():
    try:
        birth_input = input("Enter your birthdate (YYYY-MM-DD): ").strip()
        birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()

        # print("**************")
        # print(birth_date)

        today = date.today()
        this_years_birthday = birth_date.replace(year=today.year)

        # print("**************")
        # print(this_years_birthday)
        print("**************")

        if this_years_birthday < today:
            next_birthday = this_years_birthday.replace(year=today.year + 1)
        else:
            next_birthday = this_years_birthday

        days_left = (next_birthday - today).days

        # print(next_birthday - today)
        # print(type(next_birthday - today))
        # print("**************")

        print(f"Your next birthday is in {days_left} day(s) on {next_birthday.strftime('%A')}.")

    except ValueError:
        print("Invalid input! Please enter the date in YYYY-MM-DD format.")

days_until_birthday()
