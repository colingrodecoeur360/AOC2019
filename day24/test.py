import unittest
from day24.solutions import Planet1, System


class Day24(unittest.TestCase):
    def test_update_state(self):
        lines = """....#
                   #..#.
                   #..##
                   ..#..
                   #....""".split("\n")
        initial_state = [list(line.strip()) for line in lines]
        planet = Planet1(initial_state)

        planet.update_state()
        self.assertEqual("#..#.####.###.###.##.##..", planet.to_string())

        planet.update_state()
        self.assertEqual("#####....#....#...#.#.###", planet.to_string())

        planet.update_state()
        self.assertEqual("#....####....###.##..##.#", planet.to_string())

        planet.update_state()
        self.assertEqual("####.....###..#.....##...", planet.to_string())

    def test_mutate(self):
        lines = """....#
                   #..#.
                   #..##
                   ..#..
                   #....""".split("\n")
        initial_state = [list(line.strip()) for line in lines]
        planet = Planet1(initial_state)

        planet.mutate()

        self.assertEqual("...............#.....#...", planet.to_string())
        self.assertEqual(2129920, planet.biodiversity_rating)

    def test_count_bugs(self):
        lines = """....#
                   #..#.
                   #..##
                   ..#..
                   #....""".split("\n")
        initial_state = [list(line.strip()) for line in lines]
        system = System(initial_state)

        for _ in range(10):
            system.update_state()

        self.assertEqual(99, system.count_bugs())


if __name__ == '__main__':
    unittest.main()
