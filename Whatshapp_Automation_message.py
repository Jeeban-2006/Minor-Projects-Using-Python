#It is a minor project using a library twilio of Python that helps to automate message to anyone . If you need any help then refer this video : https://youtu.be/z5RwpJn86-U?si=00RzL5k_QPYMfMwL

from twilio.rest import Client
from datetime import datetime
import time

# Twilio credentials
account_sid = "Paste here your Account Sid from twilio"   #create manually
auth_token = "Paste here your Auth_token from twilio"     #create manually
client = Client(account_sid, auth_token)

# Your Twilio Sandbox WhatsApp number
from_whatsapp_number = "whatsapp:use the number that provided by twilio"  #create manually

def send_whatsapp_message(recipient_number, message):
    try:
        # Ensure number has whatsapp: prefix
        if not recipient_number.startswith("whatsapp:"):
            recipient_number = "whatsapp:" + recipient_number

        message = client.messages.create(
            from_=from_whatsapp_number,
            body=message,
            to=recipient_number
        )
        print("✅ WhatsApp message sent successfully!")
    except Exception as e:
        print("❌ Error sending WhatsApp message:", e)

# Input section
name = input("Enter the recipient's name: ")
recipient_number = input("Enter the recipient's WhatsApp number with country code (eg. +91XXXXXXXXXX): ")
message = input(f"Enter the message to send to {name}: ")

date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24-hour format): ")

# Schedule time
send_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

time_difference = (send_time - current_datetime)
delay_seconds = time_difference.total_seconds()

if delay_seconds < 0:
    print("⚠️ The specified time is in the past. Please enter a future time.")
else:
    print(f"📅 Message will be sent to {name} at {send_time.strftime('%Y-%m-%d %H:%M')}.")
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number, message)

