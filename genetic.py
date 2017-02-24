def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(guess, target)
               if expected == actual)