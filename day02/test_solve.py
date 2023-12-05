import unittest
from solve import parse_line, solve_part1, solve_part2
sample_input = [
"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]
class TestStringMethods(unittest.TestCase):

    def test_first(self):
        games = []
        for line in sample_input:
            games.append(parse_line(line))
        answer = solve_part1(games)
        self.assertEqual(answer, 8)

    def test_second(self):
        games = []
        for line in sample_input:
            games.append(parse_line(line))
        answer = solve_part2(games)
        self.assertEqual(answer, 2286)



if __name__ == '__main__':
    unittest.main()
