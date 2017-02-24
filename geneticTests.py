import unittest
import genetic

class GeneticTests(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()