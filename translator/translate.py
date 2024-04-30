# Import necessary libraries
import os
from tkinter import Tk, Label, Entry, Button

from deep_translator import GoogleTranslator
from gtts import gTTS

def translate_and_save():
    # Source and target languages
    source_language = 'en'  # Assuming English as the source language
    target_language = 'my'  # Assuming Malay as the target language

    # Input text
    input_text = input_text_entry.get()

    # Translate text
    translated_text = GoogleTranslator(source=source_language, target=target_language).translate(input_text)

    # Write translated text to a file
    with open('translated_google.txt', 'w', encoding='utf-8') as file:
        file.write(translated_text)

    # Create a gTTS object and save the audio file
    tts = gTTS(translated_text, lang=target_language)
    tts.save('translated_google.mp3')

    # Open the text and audio files
    os.startfile('translated_google.txt')
    os.startfile('translated_google.mp3')

# Create the main window
root = Tk()
root.title("English text to Myanmar Translator")

# Create input label and entry
input_label = Label(root, text="Input English text to translate:")
input_label.pack()

input_text_entry = Entry(root, width=100)
input_text_entry.pack()

# Create translate button
translate_button = Button(root, text="Translate & Save", command=translate_and_save)
translate_button.pack()

# Run the Tkinter event loop
root.mainloop()
