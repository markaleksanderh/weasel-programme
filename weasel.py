import string
from random import randint

def random_letter():
    alphabet = string.ascii_lowercase + " "
    letter = alphabet[randint(0, len(alphabet)-1)]
    return letter

def create_initial(target):
    initial = ''.join([random_letter() for i in range(len(target))])
    return initial

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
    gene_pool = [mutate(gene, chance, target) for i in range(pool_size)]
    return gene_pool

def fittest(gene_pool, target):
    target = list(target)
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
    fittest = gene_pool[i]
    return fittest

# Should return object for Flask template
def weasel(target, chance, pool_size):
    initial = create_initial(target)
    gen = initial
    fittest_in_generation = []
    while True:
        gen = generation(gen, chance, pool_size, target)
        gen = fittest(gen, target)
        print(gen)
        fittest_in_generation.append(gen)
        if gen == target:
            break
    return fittest_in_generation

# if __name__ == '__main__':
#     target = "hello world"
#     chance =  5
#     pool_size = 500
#     initial = create_initial(target)
#     gen = initial
#     fittest_in_pool = []
#     while True:
#         gen = generation(gen, chance, pool_size, target)
#         gen = fittest(gen, target)
#         fittest_in_pool.append(gen)
#         print(gen)
#         if gen == target:
#             break
#     print(fittest_in_pool)
