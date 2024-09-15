import tkinter as tk
from tkinter import PhotoImage

# Create the main application window
root = tk.Tk()
root.title("Simple Presentation App")
root.geometry("800x600")

# Define a list of slides (this can be text or images)
slides = [
    {"type": "text", "content": "Welcome to Slide 1: Introduction"},
    {"type": "text", "content": "Slide 2: Overview of our Project"},
    {"type": "image", "content": "slide3.png"},  # Make sure you have an image with this name
    {"type": "text", "content": "Slide 4: Key Takeaways"},
]

# Initialize current slide index
current_slide = 0

# Function to display text slide
def display_text_slide(content):
    slide_text.config(text=content)
    slide_text.pack(expand=True)
    slide_image.pack_forget()

# Function to display image slide
def display_image_slide(image_path):
    img = PhotoImage(file=image_path)
    slide_image.config(image=img)
    slide_image.image = img  # Keep a reference
    slide_image.pack(expand=True)
    slide_text.pack_forget()

# Function to display the current slide
def display_slide():
    slide = slides[current_slide]
    if slide["type"] == "text":
        display_text_slide(slide["content"])
    elif slide["type"] == "image":
        display_image_slide(slide["content"])

# Function to go to the next slide
def next_slide():
    global current_slide
    if current_slide < len(slides) - 1:
        current_slide += 1
        display_slide()

# Function to go to the previous slide
def prev_slide():
    global current_slide
    if current_slide > 0:
        current_slide -= 1
        display_slide()

# Create slide content elements
slide_text = tk.Label(root, text="", font=("Helvetica", 24), wraplength=600, justify="center")
slide_image = tk.Label(root)

# Create navigation buttons
prev_button = tk.Button(root, text="Previous", command=prev_slide)
next_button = tk.Button(root, text="Next", command=next_slide)

# Pack buttons at the bottom of the window
prev_button.pack(side="left", padx=20, pady=20)
next_button.pack(side="right", padx=20, pady=20)

# Display the first slide initially
display_slide()

# Start the Tkinter event loop
root.mainloop()
