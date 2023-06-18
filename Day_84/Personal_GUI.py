import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

# Function to handle button click event
def add_watermark():
    # Open the selected image file
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)

    # Get the watermark text entered by the user
    watermark_text = watermark_entry.get()

    # Add the watermark to the image
    watermark_font = ImageFont.truetype("arial.ttf", 36)
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(watermark_text, font=watermark_font)
    x = image.width - text_width - 10
    y = image.height - text_height - 10
    draw.text((x, y), watermark_text, font=watermark_font, fill=(255, 255, 255, 128))

    # Save the watermarked image
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    image.save(save_path)

    # Show a success message
    result_label.config(text="Watermark added successfully!", bg="white")


# Create the main window
window = tk.Tk()
window.title("Image Watermarking App")

# Set the background color
window.configure(bg="purple")

# Set the window size
window.geometry("500x300")  # Set the width and height as desired

# Create an entry field for the watermark text
watermark_label = tk.Label(window, text="Watermark Text:")
watermark_label.pack()
watermark_entry = tk.Entry(window)
watermark_entry.pack()

# Create a button to trigger watermarking
button = tk.Button(window, text="Add Watermark", command=add_watermark)
button.pack(pady=20)

# Create a label to display the result message
result_label = tk.Label(window, text="", bg="purple")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
