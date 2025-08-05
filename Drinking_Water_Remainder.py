import time
import winsound  # For beep sound (Windows only)

def beep_sound():
    frequency = 1000  # 1000 Hertz
    duration = 1000   # 1000 ms = 1 second
    winsound.Beep(frequency, duration)

def remind_to_drink_water():
    print("💧 Drinking water reminder started. You will be reminded every hour.")
    try:
        while True:
            time.sleep(3600)  # 1 hour = 3600 seconds
            print("🔔 Time to drink water!")
            beep_sound()
    except KeyboardInterrupt:
        print("\n👋 Reminder stopped by user. Stay hydrated!")

if __name__ == "__main__":
    remind_to_drink_water()
