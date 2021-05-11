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
    passwords = {} 
    keys = range(1, count + 1)
    for x in keys:
        password = ""
        key = 'password' + str(x)
        for i in range(1, len + 1):
            password = password + generate_character()
        passwords[key] = password
    passwords_str = str(passwords).strip("{ }")
    passwords_str = passwords_str.replace("'", "")
    passwords_str = passwords_str.replace(", ", "\n")
    return(passwords_str)

print( password_generator(12, 5))