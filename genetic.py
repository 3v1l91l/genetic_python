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

def _mutate(gene_seq, gene_set, get_fitness):
    mutate_index = random.randrange(0, len(gene_seq))
    gene_list = list(gene_seq)
    gene_new, gene_alternative = random.sample(gene_set, 2)
    gene_list[mutate_index] = gene_alternative \
        if gene_list[mutate_index] == gene_new \
        else gene_new
    gene_seq = ''.join(gene_list)

    return Chromosome(gene_seq, get_fitness(gene_seq))

def get_best(gene_set, seq_length, get_fitness, display):
    random.seed()
    best_chromosome = _generate_chromosome(gene_set, seq_length, get_fitness)
    display(best_chromosome)
    if best_chromosome.Fitness >= seq_length:
        return best_chromosome
    while True:
        mutated_chromosome = _mutate(best_chromosome.Genes, gene_set, get_fitness)
        if best_chromosome.Fitness >= mutated_chromosome.Fitness:
            continue
        display(mutated_chromosome)
        if mutated_chromosome.Fitness >= seq_length:
            return mutated_chromosome
        best_chromosome = mutated_chromosome

class Chromosome:
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness

