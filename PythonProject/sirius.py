import random

def cja(pass_length):
    wd = 'r3js0laGVL93X)aje/1!Bb'
    password = ''
    for i in range(pass_length):
        password += random.choice(wd)
    return password
