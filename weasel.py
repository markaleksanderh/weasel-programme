import string
from random import randint

def random_letter():
    alphabet = string.ascii_lowercase + " "
    letter = alphabet[randint(0, len(alphabet)-1)]
    return letter

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


def generation(gene, chance, pool_size, target):
    gene_pool = []
    for i in range(pool_size):
        gene_pool.append(mutate(gene, chance, target))
    return gene_pool


def fittest(gene_pool, target):
    # Compare against target
    # Split string
    target = list(target)
    # Keep score and index
    fittest_score = 0
    index = 0
    for i in range(len(gene_pool)):
        comp = list(gene_pool[i])
        score = 0
        for j in range(len(comp)):
            if comp[j] == target[j]:

                score = score + 1
        if score > fittest_score:
            index = i
            fittest_score = score
    return gene_pool[i]


if __name__ == '__main__':
    target = "hello world"
    chance =  10
    pool_size = 50
    initial = create_initial(target)
    gen = initial
    for i in range(500):
        gen = generation(gen, chance, pool_size, target)
        gen = fittest(gen, target)
        print(gen)
