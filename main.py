from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


BLACK = "black"
WHITE = "white"
GREY = "grey"
BLUE = "LightCyan3"
PURPLE_FONT = "purple"

# ----------------------------- PASSWORD GENERATOR --------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    check = messagebox.askyesno(title=f"{website}", message=f"Are the following details correct?\nWebsite: {website}\n"
                                                            f"Username: {email}\nPassword:{password}")
    if check:
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Open data.json file and read it, place the contents into a 'data' variable
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # If data file doesn't exist, create a new one and upload the data into it
                json.dump(new_data, data_file, indent=4)
        else:
            # Add new data to old data, and then write it in the file
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# --------------------------SEARCH FOR EXISTING ACCOUNTS--------------------------#

def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No Data File Found")
    else:
        if website in data:
            user_password = data[website]["password"]
            user_email = data[website]["email"]
            messagebox.showinfo(title=f"{website}", message=f"Website: {website}\nUsername: {user_email}\nPassword: "
                                                            f"{user_password}")
        else:
            messagebox.showerror(title="Oops", message="No details for the website exist. Try checking your spelling.")


# ---------------------------- UI SETUP ------------------------------- #
"""Create window"""
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BLUE)

"""Create Canvas and Place Image"""
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BLUE)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

"""Creating the website label & entry box"""
website_label = Label(text="Website: ", fg=BLACK, bg=BLUE)
website_label.grid(column=0, row=1)

website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.configure(bg=WHITE, fg=PURPLE_FONT, highlightthickness=0)

"""Creating the website search button"""
search_button = Button(text="Search", width=11, highlightbackground=BLUE, command=find_password)
search_button.grid(column=2, row=1)

"""Creating the email label & entry box"""
email_label = Label(text="Email/Username: ", fg=BLACK, bg=BLUE)
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.configure(fg=PURPLE_FONT, bg=WHITE, highlightthickness=0)
email_entry.insert(0, "example@gmail.com")

"""Creating the password label & entry box"""
password_label = Label(text="Password: ", fg=BLACK, bg=BLUE)
password_label.grid(column=0, row=3)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)
password_entry.configure(bg=WHITE, fg=PURPLE_FONT, highlightthickness=0)

"""Create the 'Generate Password' & 'Add' buttons"""
gen_password = Button(text="Generate Password", width=11, highlightbackground=BLUE, command=generate_password)
gen_password.grid(column=2, row=3)

add_button = Button(text="Add", width=33, highlightbackground=BLUE, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
