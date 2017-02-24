import unittest
import genetic

class GeneticTests(unittest.TestCase):
    GeneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"

    def test_get_fitness_empty_guess(self):
        expected_fitness = 0
        actual_fitness = genetic.get_fitness(guess='', target='Test')

        self.assertEqual(actual_fitness, expected_fitness)

    def test_get_fitness_empty_target(self):
        expected_fitness = 0
        actual_fitness = genetic.get_fitness(guess='Test', target='')

        self.assertEqual(actual_fitness, expected_fitness)

    def test_get_fitness_max_fitness(self):
        expected_fitness = len("Test")
        actual_fitness = genetic.get_fitness(guess='Test', target='Test')

        self.assertEqual(actual_fitness, expected_fitness)

    def test_get_fitness_medium_similarity(self):
        expected_fitness = 2
        actual_fitness = genetic.get_fitness(guess='12st', target='Test')

        self.assertEqual(actual_fitness, expected_fitness)

    def test_generate_chromosome(self):
        target = 'Test'

        def fnGetFitness(genes):
            return genetic.get_fitness(genes, target)

        actual_chromosome = genetic._generate_chromosome(self.GeneSet, len(target), fnGetFitness)

        self.assertEqual(len(actual_chromosome.Genes), len(target))
        self.assertIsNotNone(actual_chromosome.Fitness)

if __name__ == '__main__':
    unittest.main()