from collections import namedtuple

Reach = namedtuple("Reach", ["red", "green", "blue"])

class Game:

    def __init__(self, number, reaches):
        self.number: int = number
        self.reaches: list[Reach] = reaches

    def __repr__(self) -> str:
        return f"Game({self.number}, {self.reaches})"

    def is_possible(self, red, green, blue) -> bool:
        for reach in self.reaches:
            if reach.red > red or reach.green > green or reach.blue >blue:
                return False
        return True

    def smallest_set_power(self) -> int:
        red = 0
        green = 0
        blue = 0

        for reach in self.reaches:
            if reach.red > red:
                red = reach.red
            if reach.green > green:
                green = reach.green
            if reach.blue > blue:
                blue = reach.blue

        return red * green * blue

def solve_part1(games: list[Game]):
    answer = 0 
    for game in games:
        if game.is_possible(12, 13, 14):
            answer += game.number
    return answer

def solve_part2(games: list[Game]):
    answer = 0 
    for game in games:
        answer += game.smallest_set_power()
    return answer

def parse_reach(text: str) -> Reach:
    red = 0
    green = 0
    blue = 0
    for chunk in text.split(","):
        first, second = chunk.strip().split(" ")
        number = int(first)
        if "red" in second:
            red = number
        if "blue" in second:
            blue = number
        if "green" in second:
            green = number

    return Reach(red, green, blue)

def parse_line(line) -> Game:
    first, second = line.split(":")
    _, number = first.split(" ")

    reach_strings = second.split(";")
    reaches = []
    for reach_string in reach_strings:
        reach = parse_reach(reach_string)
        reaches.append(reach)
    return Game(int(number), reaches)


if __name__ == "__main__":
    games = []
    with open("input.txt") as in_file:
        for line in in_file:
            line = line.strip()
            game = parse_line(line)
            print(game)
            games.append(game)

    answer = solve_part1(games)
    print(f"Part 1: {answer}")

    answer2 = solve_part2(games)
    print(f"Part 2: {answer2}")


