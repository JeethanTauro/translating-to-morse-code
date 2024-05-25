from playsound import playsound
import time

# Function to add a delay for readability between Morse code elements
def play_with_delay(sound, delay):
    playsound(sound)
    time.sleep(delay)

# Define the Morse code dictionary
dict_morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

# Paths to sound files
dot_sound = r"C:\Users\TH\Desktop\Pandas\dotsound.wav"
dash_sound = r"C:\Users\TH\Desktop\Pandas\dashsound.wav"

# Get user input
user_text = input("Enter the words to be translated: \n").lower()
print("Translating .....")

# Set delay times (in seconds)
dot_dash_delay = 0.2  # delay between dots and dashes
letter_delay = 0.5    # delay between letters
word_delay = 1.0      # delay between words

# Translate and play Morse code
for letter in user_text:
    if letter == ' ':
        print("Space")
        time.sleep(word_delay)
        continue
    if letter in dict_morse:
        code = dict_morse[letter]
        for symbol in code:
            if symbol == '-':
                play_with_delay(dash_sound, dot_dash_delay)
            elif symbol == '.':
                play_with_delay(dot_sound, dot_dash_delay)
            else:
                print("Invalid Morse code symbol")
        time.sleep(letter_delay)
    else:
        print(f"Unsupported character: {letter}")

print("Translation done!!")
