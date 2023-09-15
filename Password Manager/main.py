from tkinter import *
from tkinter import messagebox
import random
import json

# pyperclip to copy paste password otomatis don't forget


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {website: {"email": email, "password": password}}

    if website == "" or email == "" or password == "":
        missing = messagebox.showerror(
            title="Ooops!", message="Please don't leave any fields empty!"
        )
    else:
        messagebox.showinfo(
            title="Success", message=f"Added {website} to the data store."
        )
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# --------------------------- SEARCH WEB ------------------------------ #
def search_website():
    name_website = website_input.get()
    with open("data.json", "r") as file:
        data = json.load(file)  
    try:
        website = data[name_website]
    except KeyError:
        messagebox.showerror(
            title="Data not found",
            message=f"Data: {name_website} not found in the data store.",
        )
    except FileNotFoundError:
        messagebox.showerror(
            title="Data not found",
            message=f"Data: {name_website} not found in the data store.",
        )
    else:
        messagebox.showinfo(
            title=f"{name_website}",
            message=f"Email: {website['email']}\nPassword: {website['password']}",
        )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")
image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
website_input = Entry(width=29, bg="white")
website_input.focus()
website_input.grid(row=1, column=1)
search_button = Button(command=search_website, text="Search", bg="white", width=15)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)
email_input = Entry(width=49, bg="white")
email_input.insert(0, "choirunnizam175@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)
password_input = Entry(bg="white", width=29)
password_input.grid(row=3, column=1, columnspan=1)

generate_button = Button(command=pass_generator, text="Generate Password", bg="white")
generate_button.grid(row=3, column=2, columnspan=1)
add_button = Button(command=save_pass, text="Add", width=45, bg="white")
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
