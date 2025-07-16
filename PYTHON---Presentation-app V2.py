import tkinter as tk
from tkinter import PhotoImage

# Create the main application window
root = tk.Tk()
root.title("Simple Presentation App")
root.geometry("800x600")

# Define a list of slides
slides = [
    {"type": "text", "content": "Welcome to Slide 1: Introduction"},
    {"type": "text", "content": "Slide 2: Overview of our Project"},
    {"type": "image", "content": "slide3.png"},  # Ensure this file exists
    {"type": "text", "content": "Slide 4: Key Takeaways"},
]

current_slide = 0

# Function to display text slide
def display_text_slide(content):
    slide_text.config(text=content)
    slide_text.pack(expand=True)
    slide_image.pack_forget()

# Function to display image slide
def display_image_slide(image_path):
    try:
        img = PhotoImage(file=image_path)
        slide_image.config(image=img)
        slide_image.image = img
        slide_image.pack(expand=True)
        slide_text.pack_forget()
    except Exception as e:
        slide_text.config(text=f"Image not found: {image_path}")
        slide_text.pack(expand=True)
        slide_image.pack_forget()

# Display current slide
def display_slide():
    slide = slides[current_slide]
    if slide["type"] == "text":
        display_text_slide(slide["content"])
    elif slide["type"] == "image":
        display_image_slide(slide["content"])
    update_status()

# Next slide
def next_slide():
    global current_slide
    if current_slide < len(slides) - 1:
        current_slide += 1
        display_slide()

# Previous slide
def prev_slide():
    global current_slide
    if current_slide > 0:
        current_slide -= 1
        display_slide()

# NEW FUNCTION 1: Jump to specific slide
def jump_to_slide(index):
    global current_slide
    if 0 <= index < len(slides):
        current_slide = index
        display_slide()

# NEW FUNCTION 2: Restart presentation
def restart_presentation():
    global current_slide
    current_slide = 0
    display_slide()

# NEW FUNCTION 3: Update slide number info
def update_status():
    status_label.config(text=f"Slide {current_slide + 1} of {len(slides)}")

# NEW FUNCTION 4: Keyboard navigation
def key_pressed(event):
    if event.keysym == "Right":
        next_slide()
    elif event.keysym == "Left":
        prev_slide()

# Create UI elements
slide_text = tk.Label(root, text="", font=("Helvetica", 24), wraplength=600, justify="center")
slide_image = tk.Label(root)
status_label = tk.Label(root, text="", font=("Helvetica", 12), pady=10)

prev_button = tk.Button(root, text="Previous", command=prev_slide)
next_button = tk.Button(root, text="Next", command=next_slide)
restart_button = tk.Button(root, text="Restart", command=restart_presentation)
jump_entry = tk.Entry(root, width=5)
jump_button = tk.Button(root, text="Go to Slide", command=lambda: jump_to_slide(int(jump_entry.get()) - 1))

# Pack buttons and UI
prev_button.pack(side="left", padx=20, pady=20)
next_button.pack(side="right", padx=20, pady=20)
restart_button.pack(side="bottom", pady=10)
jump_entry.pack(side="left", padx=5)
jump_button.pack(side="left")
status_label.pack(side="bottom")

# Keyboard bindings
root.bind("<Left>", key_pressed)
root.bind("<Right>", key_pressed)

# Display the first slide
display_slide()

# Start the Tkinter loop
root.mainloop()
