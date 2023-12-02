
def part1_get_digits(line: str) -> list[str]:
    return list(i for i in line if i.isdigit())

def part2_get_digits(line: str) -> list[str]:
    line = line.replace("eightwo", "82")
    line = line.replace("eighthree", "83")

    line = line.replace("oneight", "18")
    line = line.replace("threeight", "38")
    line = line.replace("fiveight", "58")
    line = line.replace("nineight", "98")

    line = line.replace("twone", "21")

    line = line.replace("sevenine", "79")

    line = line.replace("one", "1")
    line = line.replace("two", "2")
    line = line.replace("three", "3")
    line = line.replace("four", "4")
    line = line.replace("five", "5")
    line = line.replace("six", "6")
    line = line.replace("seven", "7")
    line = line.replace("eight", "8")
    line = line.replace("nine", "9")
    return list(i for i in line if i.isdigit())

def solve_part_1(lines: list[str]) -> int:
    total = 0
    for line in lines:
        digits = part1_get_digits(line)
        s = digits[0] + digits[-1]
        total += int(s)

    return total

def solve_part_2(lines: list[str]) -> int:
    total = 0
    for line in lines:
        digits = part2_get_digits(line)
        s = digits[0] + digits[-1]
        total += int(s)
    return total


if __name__ == "__main__":
    lines = []

    with open("input.txt") as infile:
        for line in infile:
            lines.append(line.strip())


    print(f"Part1: {solve_part_1(lines)}")
    print(f"Part2: {solve_part_2(lines)}")


