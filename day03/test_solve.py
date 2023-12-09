import unittest
from solve import solve1, solve2

test_lines = [
"467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598..",
]

class TestStringMethods(unittest.TestCase):

    def test_solve1(self):
        answer = solve1(test_lines)
        self.assertEqual(answer, 4361)
    
    def test_solve2(self):
        answer = solve2(test_lines)
        self.assertEqual(answer, 467835)

if __name__ == '__main__':
    unittest.main()
