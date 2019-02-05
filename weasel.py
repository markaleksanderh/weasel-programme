import string
from time import sleep
from random import randint
alphabet = string.ascii_lowercase + " "
from copy import deepcopy

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

def mutate(gene, chance, target):
    gene = list(gene)
    for i in range(len(gene)):
        if gene[i] != target[i]:
            n = randint(0, 100)
            if n < chance:
                gene[i] = random_letter()
    gene = ''.join(gene)
    return gene


def generation():
    pass

def fittest():
    pass

if __name__ == '__main__':
    target = "hello"
    chance =  5
    initial = create_initial(target)
    gen = initial
    # print(initial + " ------------- initial")
    for i in range(500):
        gen = mutate(gen, chance, target)
        print(target + "-- target")
        print(gen + "-- gen")
        # print(gene + " << main")
        # print(initial + "-- init")
        # sleep(0.5)
