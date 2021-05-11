import tkinter as tk
from scipy.stats import norm
import random

chars = "abcdefghijklmnopqrstuvwxyz"
upr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
spec_char = "?!#$%&()[]+="

def generate_character():
    value = norm.rvs(size = 1) 
    if 0 <= value < 1 : 
        x = password_char = random.choice(chars) 
    elif -1.2 <= value < 0: 
        x = password_char = random.choice(upr) 
    elif 1 <= value: 
        x = password_char = random.choice(num) 
    else: 
        x = password_char = random.choice(spec_char) 
    return x

def password_generator(len = 12, count = 1):
    if (len <= 0 or len > 25) and (count <= 0):
        passwords_str = "Invalid password length and password count"
    elif (len <= 0 or len > 25) and (count > 0):
        passwords_str = "Invalid password length"
    elif (count <= 0) and (0 < len <= 25):
        passwords_str = "Invalid password count"
    else:
        generate_text.set("Working")
        passwords = {} 
        keys = range(1, count + 1)
        for x in keys:
            password = ""
            key = 'password' + str(x)
            for i in range(1, len + 1):
                password = password + generate_character()
            passwords[key] = password
        generate_text.set("Generate Passwords")
        passwords_str = str(passwords).strip("{ }")
        passwords_str = passwords_str.replace("'", "")
        passwords_str = passwords_str.replace(", ", "\n")

    #textbox
    text_box = tk.Text(root, height = 10, width = 50)
    text_box.insert(1.0, passwords_str)
    text_box.grid(columnspan=2, row = 4)

root = tk.Tk()
root.title("Password Generator")

canvas = tk.Canvas(root, width = 750, height = 500, bg = "#28313F")
canvas.grid(columnspan = 2, rowspan = 5)

#instructions
instructions = tk.Label(root, 
    text = """Choose the length of your passwords and how many you want genorated (having more will give you more options to choose from) 
    \n I recomend about 5 passwords at a time
    \n
    \n Password length can be any integer between 1 and 25.
    \n Password count must be a positive integer.""",
    bg = "#28313F",
    fg = "white"
    )
instructions.grid(columnspan = 2, row = 0)

#input
password_len = tk.IntVar()
password_count = tk.IntVar()

pl_lable = tk.Label(root, text = "Password length", bg = "#28313F", fg = "white")
pl = tk.Entry(root, textvariable = password_len)
pl_lable.grid(column = 0, row = 1)
pl.grid(column = 1, row = 1)

pc_lable = tk.Label(root, text = "Amount of passwords", bg = "#28313F", fg = "white")
pc = tk.Entry(root, textvariable = password_count)
pc_lable.grid(column = 0, row = 2)
pc.grid(column = 1, row = 2)

#recomended values
password_len.set(12)
password_count.set(5)

#generate button
generate_text = tk.StringVar()
generate_btn = tk.Button(root, textvariable = generate_text, 
    command = lambda:password_generator(password_len.get(), password_count.get()), 
    bg = "#4682B4", fg = "white", height = 2, width = 15
    )
generate_text.set("Generate Passwords")
generate_btn.grid(columnspan = 2, row = 3)


root.mainloop()