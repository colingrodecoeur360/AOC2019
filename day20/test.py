import unittest
from day20.solutions import compute_shortest_path


class Day20(unittest.TestCase):
    def test_compute_shortest_path(self):
        self.assertEqual(23, compute_shortest_path(test_cases[0]))


test_cases = {
    0: """         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z     """.split("\n")
}

if __name__ == '__main__':
    unittest.main()
