import string
from random import randint
alphabet = string.ascii_lowercase + " "

def random_letter():
    alphabet = string.ascii_lowercase + " "
    rand_letter = alphabet[randint(0, len(alphabet)-1)]
    return rand_letter


def create_initial(target):
    # REFACTOR
    length = len(target)
    initial = []
    for i in range(length):
        initial.append(random_letter())
    return ''.join(initial)

def mutate(str, chance, target):
    # REFACTOR
    str = list(str)
    mutated = []
    for i in range(len(str)):
        if str[i] == target[i]:
            mutated.append(str[i])
        else:
            random = randint(0, 100)
            if random < chance:
                mutated.append(random_letter())
            else:
                mutated.append(str[i])
    return ''.join(mutated)

def generation():
    pass

def fittest():
    pass

if __name__ == '__main__':
    target = "some target string"
    chance =  5
    initial = create_initial(target)
    for i in range(10):
        print(mutate(initial, chance, target))
