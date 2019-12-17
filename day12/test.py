import unittest
from day12.solutions import System


class Day12(unittest.TestCase):
    def test_compute_system_energy(self):
        system = System(test_cases[0])
        system.update_state_multiple_times(10)
        self.assertEqual(179, system.energy)

        system = System(test_cases[1])
        system.update_state_multiple_times(100)
        self.assertEqual(1940, system.energy)

    def test_compute_period(self):
        system = System(test_cases[0])
        period = system.compute_period()
        self.assertEqual(2772, period)

        system = System(test_cases[1])
        period = system.compute_period()
        self.assertEqual(4686774924, period)


test_cases = {
    0: """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""".split("\n"),
    1: """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>""".split("\n")
}

if __name__ == '__main__':
    unittest.main()
