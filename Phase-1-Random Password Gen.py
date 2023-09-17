import tkinter as tk
from tkinter import *
import random
import string
from PIL import *
from PIL import Image, ImageTk, ImageFilter
import requests
from io import BytesIO

#Create the Main Window
root = Tk()
root.title("Random Password Generator")
root.geometry("800x600")

# Define custom colors
bg_color = "#1E3B4D"  # Background color
text_color = "#F5F5F5"  # Text color
button_bg = "#367f59"  # Button background color
checkbox_bg = "#fe9037"  # Checkbox background color
result_color = "#F3872F"  # Result label text color

# Set the background color of the main window
root.configure(bg=bg_color)

# Fetch and display an image from a URL
image_url = "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA12s2Nq.img"  # Replace with your image URL
response = requests.get(image_url)
img_data = response.content
image = Image.open(BytesIO(img_data))

#image = image.resize((800, 600), Image.ANTIALIAS)  # Resize the image to fit the window

# Apply a blur effect to the image
image = image.filter(ImageFilter.BLUR)

# Resize the image to fit the window
image = image.resize((800, 600))

header_image = ImageTk.PhotoImage(image)

header_label = Label(root, image=header_image)
header_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a custom font
custom_font = ("Helvetica", 14)

# Random Password Generator Section
generator_frame = Frame(root, bg="white", bd=5)
generator_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)  # Covers 90% of the image

# Create a style for labels
label_style = {"bg": bg_color, "fg": text_color, "font": custom_font}

# Create a style for checkboxes
checkbox_style = {"bg": checkbox_bg, "fg": text_color}

# Create a style for the result label
result_label_style = {"bg": bg_color, "fg": result_color, "font": custom_font}

#Create Variables for User Inputs
password_length = IntVar()
password_length.set(12)  # Default password length
use_lowercase = BooleanVar()
use_uppercase = BooleanVar()
use_digits = BooleanVar()
use_special_chars = BooleanVar()


#Define Functions to Generate Password
def generate_password():
    length = password_length.get()
    chars = ""
    
    if use_lowercase.get():
        chars += string.ascii_lowercase
    if use_uppercase.get():
        chars += string.ascii_uppercase
    if use_digits.get():
        chars += string.digits
    if use_special_chars.get():
        chars += string.punctuation
    
    if not chars:
        result_label.config(text="Please select at least one character type.")
    else:
        password = ''.join(random.choice(chars) for _ in range(length))
        result_label.config(text="Generated Password: " + password)

# Create GUI Elements
# Password Length Label and Entry
length_label = Label(generator_frame, text="Password Length:", font=custom_font)
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
length_entry = Entry(generator_frame, textvariable=password_length, font=custom_font, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Character Type Checkboxes
lowercase_check = Checkbutton(generator_frame, text="Lowercase", variable=use_lowercase, font=custom_font)
lowercase_check.grid(row=1, column=0, padx=10, pady=10, sticky="w")
uppercase_check = Checkbutton(generator_frame, text="Uppercase", variable=use_uppercase, font=custom_font)
uppercase_check.grid(row=1, column=1, padx=10, pady=10, sticky="w")
digits_check = Checkbutton(generator_frame, text="Digits", variable=use_digits, font=custom_font)
digits_check.grid(row=2, column=0, padx=10, pady=10, sticky="w")
special_chars_check = Checkbutton(generator_frame, text="Special Characters", variable=use_special_chars, font=custom_font)
special_chars_check.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Generate Password Button
generate_button = Button(generator_frame, text="Generate Password", command=generate_password, font=custom_font)
generate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Result Label
result_label = Label(generator_frame, text="", font=custom_font)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Main Loop
root.mainloop()
