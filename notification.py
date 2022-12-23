import random
import time
import tkinter as tk

# Constants for the notification time (Nepal Standard Time)
NOTIFY_HOUR = 17  # 5 PM
NOTIFY_MINUTE = 0
NOTIFY_SECOND = 0

# Load the questions from the text file
with open("questions.txt", "r") as f:
    questions = f.readlines()

# Select a random question from the list of questions
question = random.choice(questions)

def show_notification():
    # Create the notification window
    window = tk.Tk()
    window.title("Question Notification")
    window.geometry("250x100")

    # Add a label with the selected question
    label = tk.Label(window, text=f"It's time to solve the following question:\n{question}")
    label.pack()

    # Add an "OK" button to close the window
    button = tk.Button(window, text="OK", command=window.destroy)
    button.pack()

# Wait until the notification time
while True:
    current_time = time.localtime()
    if (current_time.tm_hour == NOTIFY_HOUR and
        current_time.tm_min == NOTIFY_MINUTE and
        current_time.tm_sec == NOTIFY_SECOND):
        break
    time.sleep(1)  # Sleep for 1 second before checking the time again

# Show the notification window
show_notification()
