from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# Added a timer delay to give you time to click to where you want in a browser or notepad
time.sleep(4)

# creating a message to be displayed
message = "insert any text here"

# splitting the message using .split()
words = message.split()

# grouping the words
chunklist = [' '.join(words[i: i + 10]) for i in range(0, len(words), 10)]

# printing the spam line by line
for items in chunklist:
    keyboard.type(items)
    # assuming it is being printed somewhere where enter either sends a message or makes a new line
    keyboard.press(Key.enter)
    time.sleep(1)
