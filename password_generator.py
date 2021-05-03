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
    elif -1 <= value < 0: 
        x = password_char = random.choice(num) 
    elif 1 <= value: 
        x = password_char = random.choice(upr) 
    else: 
        x = password_char = random.choice(spec_char) 
    return x

pword_len = int(input("How long would you like your password to be? "))
pword_count = int(input("How many passwords would you like generated? "))

for x in range(0, pword_count) :
    password = ""
    for i in range(0, pword_len) :
        password = password + generate_character()
    print('Password ', x+1, ': ', password)