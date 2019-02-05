import string
from random import randint
alphabet = string.ascii_lowercase + " "

def create_initial(target):
    # Refactor later
    length = len(target)
    initial = []
    for i in range(length):
        initial.append(alphabet[randint(0, len(alphabet)-1)])
    return ''.join(initial)

def mutate(str, chance):
    pass

def generation():
    pass

def fittest():
    pass

if __name__ == '__main__':
    target = "some target string"
    chance =  0.5
    print(create_initial(target))


#
# class Mutation:
#     initial = ""
#
