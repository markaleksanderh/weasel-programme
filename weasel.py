import string
from random import randint
alphabet = string.ascii_lowercase + " "

def create_initial(target):
    # REFACTOR
    length = len(target)
    initial = []
    for i in range(length):
        initial.append(alphabet[randint(0, len(alphabet)-1)])
    return ''.join(initial)

def mutate(str, chance):
    # REFACTOR
    # If character is the same as character in same position of target string, do not change
    str = list(str)
    mutated = []
    for i in str:
        random = randint(0, 100)
        if random < 5:
            mutated.append('!')
        else:
            mutated.append(i)
    return ''.join(mutated)

def generation():
    pass

def fittest():
    pass

if __name__ == '__main__':
    target = "some target string"
    chance =  5
    initial = create_initial(target)
    print(mutate(initial, chance))
