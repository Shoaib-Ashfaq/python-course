import time
import datetime
import os

def play_sound():
    try:
        if os.name == 'nt':
            import winsound
            winsound.Beep(1000, 1000)
        else:
            os.system('say "Time is up!"')
    except:
        print("Sound could not be played.")

def set_timer(seconds):
    print(f" Timer set for {seconds} seconds.")
    time.sleep(seconds)
    print(" Timer finished!")
    play_sound()

def set_alarm(alarm_time_str):
    try:
        now = datetime.datetime.now()
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")

        alarm_time = now.replace(hour=alarm_time.hour, minute=alarm_time.minute, second=0, microsecond=0)

        if alarm_time < now:
            alarm_time += datetime.timedelta(days=1)

        wait_seconds = (alarm_time - now).total_seconds()
        print(f" Alarm set for {alarm_time.strftime('%H:%M')}. Waiting...")

        time.sleep(wait_seconds)
        print("Alarm ringing!")
        play_sound()

    except ValueError:
        print("Invalid time format. Use HH:MM (24-hour clock).")


print("Choose an option:")
print("1. Set a timer (in seconds)")
print("2. Set an alarm (HH:MM)")

choice = input("Enter 1 or 2: ")

if choice == '1':
    try:
        seconds = int(input("Enter number of seconds: "))
        set_timer(seconds)
    except ValueError:
        print("Please enter a valid number.")
elif choice == '2':
    alarm_time = input("Enter alarm time in HH:MM format: ")
    set_alarm(alarm_time)
else:
    print("Invalid choice.")
