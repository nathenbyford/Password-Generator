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

def password_generator(len, count):
    for x in range(0, count) :
        password = ""
        for i in range(0, len) :
            password = password + generate_character()
        print('Password ', x+1, ': ', password)

root = tk.Tk()
root.title("Password Generator")

canvas = tk.Canvas(root, width = 750, height = 500)
canvas.grid(columnspan = 3, rowspan = 4)

#instructions
instructions = tk.Label(root, text = "Choose the length of your passwords and how many you want genorated")
instructions.grid(columnspan = 3, row = 0)

#input
password_len = tk.IntVar()
password_count = tk.IntVar()

pl_lable = tk.Label(root, text = "Password length")
pl = tk.Entry(root, textvariable = password_len)
pl_lable.grid(column = 0, row = 1)
pl.grid(column = 1, row = 1)

pc_lable = tk.Label(root, text = "Amount of passwords")
pc = tk.Entry(root, textvariable = password_count)
pc_lable.grid(column = 0, row = 2)
pc.grid(column = 1, row = 2)
    

root.mainloop()