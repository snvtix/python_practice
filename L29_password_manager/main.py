import tkinter as tk
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    
    shuffle(password_list)
    password = "".join(password_list)
    input_pass.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    path = "L29_password_menager/passwords.txt"

    web = input_web.get()
    user = input_user.get()
    password = input_pass.get()

    if web and password:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nUser: {user} \nPassword: {password} \nSave?")

        if is_ok:
            with open(path, "a") as file:
                file.write(f"{web} / {user} / {password}\n")
                input_web.delete(0, END)
                input_pass.delete(0, END)
    else: 
        messagebox.showerror(title="Error", message="Incomplete data, please try again")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password menager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="L29_password_menager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label_web= tk.Label(window, text="Website:", font=("Courier", 10, "bold"))
label_web.grid(row=1, column=0)
label_user = tk.Label(window, text="Email/Username:", font=("Courier", 10, "bold"))
label_user.grid(row=2, column=0)
label_pass = tk.Label(window, text="Password:", font=("Courier", 10, "bold"))
label_pass.grid(row=3, column=0)

input_web = tk.Entry(width=45)
input_web.grid(row=1, column=1, columnspan=2)
input_web.focus()
input_user = tk.Entry(width=45)
input_user.grid(row=2, column=1, columnspan=2)
input_user.insert(0, "natalia@gmail.com")
input_pass = tk.Entry(width=32)
input_pass.grid(row=3, column=1)

generate_button = tk.Button(window, text="Generate", font=("Courier", 10, "bold"), highlightthickness=0, command=generate)
generate_button.grid(row=3, column=2)
add_button = tk.Button(window, text="Add", width=34, font=("Courier", 10, "bold"), highlightthickness=0, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()