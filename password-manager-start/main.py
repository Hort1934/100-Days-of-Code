from tkinter import *
import random
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    text_3.insert(0, password)
    pyperclip(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_click():
    text_1_ = text_1.get()
    text_2_ = text_2.get()
    text_3_ = text_3.get()

    if len(text_1_) == 0 or len(text_3_) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=text_1_, message=f"These are the details entered: \nEmail: {text_2_}"
                                                              f"\nPassword: {text_3_} \nIs it ok to save?")

        with open("data.txt", "a") as file:
            file.write(f"{text_1_} | {text_2_} | {text_3_}\n")
            text_1.delete(0, END)
            text_3.delete(0, END)
            file.close()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, background="#FFFFFF")

canvas = Canvas(width=200, height=200, background="#FFFFFF", highlightthickness=0)
password_manager = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_manager)
canvas.grid(column=1, row=0)

label_1 = Label(text="Website:  ", highlightthickness=0, background="#FFFFFF")
label_1.grid(column=0, row=1)

label_2 = Label(text="Email/Username:", highlightthickness=0, background="#FFFFFF")
label_2.grid(column=0, row=2)

label_3 = Label(text="Password:", highlightthickness=0, background="#FFFFFF")
label_3.grid(column=0, row=3)

text_1 = Entry(width=35)
text_1.grid(column=1, row=1, columnspan=2)
text_1.focus()

text_2 = Entry(width=35)
text_2.grid(column=1, row=2, columnspan=2)
text_2.insert(0, "marchenko@gmail.com")

text_3 = Entry(width=21)
text_3.grid(column=1, row=3)

button_1 = Button(text="Generate Password", command=create_password)
button_1.grid(column=2, row=3, columnspan=2)

button_2 = Button(text="Add", width=36, command=add_click)
button_2.grid(column=1, row=4, columnspan=2)

window.mainloop()
