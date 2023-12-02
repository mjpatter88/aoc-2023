import unittest
from solve import solve_part_1, solve_part_2

part1_lines = [
"1abc2",
"pqr3stu8vwx",
"a1b2c3d4e5f",
"treb7uchet",
]

part2_lines = [
"two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen",
]

class TestSolver(unittest.TestCase):

    def test_part1(self):
        part1 = solve_part_1(part1_lines);
        self.assertEqual(part1, 142)

    def test_part2(self):
        part1 = solve_part_2(part2_lines);
        self.assertEqual(part1, 281)

if __name__ == "__main__":
    unittest.main()
