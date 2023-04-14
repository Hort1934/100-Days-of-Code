import tkinter
import turtle

window = tkinter.Tk()
window.title("My First GUI Progrram")
window.minsize(600, 600)
window.config(padx=10, pady=10)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "bold"))
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=1, row=0)
# my_label["text"] = "New Text"
# my_label.config(text="New Text")


def button_click():
    print("I got clicked")
    my_label.config(text=input.get())


# Button
button_1 = tkinter.Button(text="Click Me", command=button_click)
button_2 = tkinter.Button(text="Click Me Again", command=button_click)
button_1.grid(column=2, row=0)
button_2.grid(column=1, row=1)
# button.pack()
# tim = turtle.Turtle()
# tim.write("Some text", font=("Times New Roman", 80))

# Entry
input = tkinter.Entry(width=10)
input.get()
input.grid(column=3, row=2)
# input.pack()

# Text

# Spindox

# Scale
#
#
#




window.mainloop()
