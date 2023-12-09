SYMBOL_CHARS = "!@#$%^&*()-_=+[{]}/?"

def is_symbol_adjacent(symbols, location, length) -> bool:
    row = location[0]
    col = location[1]
    left_side = [(row-1, col-1), (row, col-1), (row+1, col-1)]
    top = []
    for column in range(col, col + length):
        top.append((row-1, column))
    end = col + length - 1
    right_side = [(row-1, end+1), (row, end+1), (row+1, end+1)]
    bottom = []
    for column in range(col, col + length):
        bottom.append((row+1, column))

    matches = left_side + top + bottom + right_side
    for match in matches:
        if match in symbols:
            return True
    return False

def get_adjacent_part_numbers(part_nums, location):
    adjacent_parts = []

    for part_num in part_nums:
        if is_symbol_adjacent([location], part_num[1], len(part_num[0])):
            adjacent_parts.append(part_num)

    return adjacent_parts

def solve1(lines: list[str]) -> int:
    # each holds tuples of the part # and the starting coordinate (row, col)
    part_nums = []
    # each holds tuples of the location (row, col) of a symbol
    symbols = []

    for row_num, line in enumerate(lines):
        part_number = ""
        start = None
        for col_num, char in enumerate(line):
            if char.isdigit():
                part_number += char
                if not start:
                    start = (row_num, col_num)
            else:
                if start is not None:
                    part_nums.append((part_number, start))
                    part_number = ""
                    start = None
            if char in SYMBOL_CHARS:
                symbols.append((row_num, col_num))

    total = 0
    for part_num in part_nums:
        if is_symbol_adjacent(symbols, part_num[1], len(part_num[0])):
            total += int(part_num[0])

    return total

def solve2(lines: list[str]) -> int:
    # each holds tuples of the part # and the starting coordinate (row, col)
    part_nums = []
    # each holds tuples of the location (row, col) of a gear
    gears = []

    for row_num, line in enumerate(lines):
        part_number = ""
        start = None
        for col_num, char in enumerate(line):
            if char.isdigit():
                part_number += char
                if not start:
                    start = (row_num, col_num)
            else:
                if start is not None:
                    part_nums.append((part_number, start))
                    part_number = ""
                    start = None
            if char == "*":
                gears.append((row_num, col_num))

    total = 0
    for gear in gears:
        adjacent_parts = get_adjacent_part_numbers(part_nums, gear)
        print(f"{gear}: {len(adjacent_parts)}")
        if len(adjacent_parts) == 2:
            total += (int(adjacent_parts[0][0]) * int(adjacent_parts[1][0]))

    return total

def main():
    lines = []
    with open("input.txt") as in_file:
        lines = in_file.readlines()

    answer1 = solve1(lines)
    answer2 = solve2(lines)

    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")


if __name__ == "__main__":
    main()
