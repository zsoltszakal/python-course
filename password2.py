from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

#---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generator():
    pass_input.delete(0, END)
    nr_letters = random.randint(8, 10)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    nr_symbols = random.randint(2, 4)
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    nr_numbers = random.randint(2, 4)
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_pre = password_number + password_letters + password_symbols

    random.shuffle(password_pre)

    password = "".join(password_pre)

    pass_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        web: {
            "email": email,
            "password": password
    }}

    if len(web) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Sorry, web address or password missing")
    else:
        try:
            with open("password.json", "r") as pass_file:
                #Reading old data
                data = json.load(pass_file)
                #Updating old data with new data
                data.update(new_data)

            with open("password.json", "w") as pass_file:
                #Saving new data
                json.dump(data, pass_file, indent=4)
        except FileNotFoundError:
            with open("password.json", "w") as pass_file:
                #Saving new data
                json.dump(new_data, pass_file, indent=4)
        else:
            web_input.delete(0, END)
            pass_input.delete(0, END)

def search():
    web = web_input.get()
    try:
        with open("password.json", "r") as pass_file:
            data = json.load(pass_file)
            your_email = data[web]["email"]
            your_pass = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {your_email}, \n Password: {your_pass}")
    except FileNotFoundError:
        messagebox.showinfo(title=web, message=f"Please save password first")
    except KeyError:
        messagebox.showinfo(title=web, message=f"Please enter website")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="key.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0)

web_input = Entry(width=50, justify="left")
web_input.grid(row=1, column=1, columnspan=3, pady=5)
web_input.focus()


email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2, pady=5)
email_input.insert(0, "zsltszakal@gmail.com")

pass_input = Entry(width=30)
pass_input.grid(row=3, column=1)

check_button = Button(text="Search", command=search)
check_button.grid(row=1, column=4, pady=10)

pass_button = Button(text="Generate Password", command=generator)
pass_button.grid(row=3, column=2, pady=10)

add_button = Button(text="Add", width=40, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()
