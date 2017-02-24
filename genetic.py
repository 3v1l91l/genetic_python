import random

def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(guess, target)
               if expected == actual)

def _generate_chromosome(gene_set, seq_length, get_fitness):
    gene_list = []
    while len(gene_list) < seq_length:
        sample_length = min(len(gene_set), seq_length - (len(gene_list)))
        gene_list.extend(random.sample(gene_set, sample_length))

    genes = ''.join(gene_list)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)

class Chromosome:
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness

