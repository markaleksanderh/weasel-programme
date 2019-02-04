'''
User created target string
Iterate through target string
Each character has % chance of mutation
Join
'''
import string
from random import randint
alphabet = string.ascii_lowercase + " "

target = "some target string"


def create_initial(target):
    length = len(target)
    initial = []
    for i in range(length):
        initial.append(alphabet[randint(0, len(alphabet)-1)])
    return ''.join(initial)

print(create_initial(target))
