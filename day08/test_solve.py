
import unittest
from solve import parse_input, solve1, solve2

test_lines = [
"RL",
"",
"AAA = (BBB, CCC)",
"BBB = (DDD, EEE)",
"CCC = (ZZZ, GGG)",
"DDD = (DDD, DDD)",
"EEE = (EEE, EEE)",
"GGG = (GGG, GGG)",
"ZZZ = (ZZZ, ZZZ)",
]

test_lines_repeat = [
"LLR",
"",
"AAA = (BBB, BBB)",
"BBB = (AAA, ZZZ)",
"ZZZ = (ZZZ, ZZZ)",
]

class TestStringMethods(unittest.TestCase):

    def test_solve1(self):
        map = parse_input(test_lines)
        answer = solve1(map)
        self.assertEqual(answer, 2)

    def test_solve1_repeat(self):
        map = parse_input(test_lines_repeat)
        answer = solve1(map)
        self.assertEqual(answer, 6)
    
    # def test_solve2(self):
    #     answer = solve2(test_lines)
    #     self.assertEqual(answer, 467835)

if __name__ == '__main__':
    unittest.main()
