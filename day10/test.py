import unittest
from day10.solutions import compute_max_visible_asteroids, compute_nth_hit_answer


class Day10(unittest.TestCase):
    def test_compute_max_visible_asteroids(self):
        self.assertEqual(8, compute_max_visible_asteroids(build_grid(test_cases[0])))
        self.assertEqual(35, compute_max_visible_asteroids(build_grid(test_cases[2])))
        self.assertEqual(41, compute_max_visible_asteroids(build_grid(test_cases[3])))
        self.assertEqual(210, compute_max_visible_asteroids(build_grid(test_cases[4])))

    def test_compute_nth_hit_answer(self):
        self.assertEqual(802, compute_nth_hit_answer(build_grid(test_cases[4])))


def build_grid(test_case):
    return [list(x.strip()) for x in test_case.split("\n")]


test_cases = {
    0: """.#..#
    .....
    #####
    ....#
    ...##""",
    1: """......#.#.
    #..#.#....
    ..#######.
    .#.#.###..
    .#..#.....
    ..#....#.#
    #..#....#.
    .##.#..###
    ##...#..#.
    .#....####""",
    2: """#.#...#.#.
    .###....#.
    .#....#...
    ##.#.#.#.#
    ....#.#.#.
    .##..###.#
    ..#...##..
    ..##....##
    ......#...
    .####.###.""",
    3: """.#..#..###
    ####.###.#
    ....###.#.
    ..###.##.#
    ##.##.#.#.
    ....###..#
    ..#.#..#.#
    #..#.#.###
    .##...##.#
    .....#.#..""",
    4: """.#..##.###...#######
    ##.############..##.
    .#.######.########.#
    .###.#######.####.#.
    #####.##.#.##.###.##
    ..#####..#.#########
    ####################
    #.####....###.#.#.##
    ##.#################
    #####.##.###..####..
    ..######..##.#######
    ####.##.####...##..#
    .#####..#.######.###
    ##...#.##########...
    #.##########.#######
    .####.#.###.###.#.##
    ....##.##.###..#####
    .#.#.###########.###
    #.#.#.#####.####.###
    ###.##.####.##.#..##""",
}

if __name__ == '__main__':
    unittest.main()
