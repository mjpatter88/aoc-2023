from itertools import cycle


class Map:

    def __init__(self, instructions, network) -> None:
        self.instructions = instructions
        self.network = network
        
        self._instr_iter = cycle(self.instructions)
        self._current_node = "AAA"
    
    def next(self):
        instr = next(self._instr_iter)
        node = self.network[self._current_node]
        if instr == "L":
            self._current_node = node[0]
        elif instr == "R":
            self._current_node = node[1]
        else:
            raise RuntimeError(f"Illegal Instruction: {instr}")
        return self._current_node
    
    def __repr__(self) -> str:
        return f"Map(instructions: {self.instructions}, network: {self.network})"


def solve2(map: Map) -> int:
    return 0

def solve1(map: Map) -> int:
    counter = 1
    while map.next() != "ZZZ":
        counter += 1
    return counter

def parse_input(lines: list[str]) -> Map:
    instructions = list(lines[0].strip())
    # name -> (left, right)
    network = dict()

    for line in lines[2:]:
        first, second = line.split("=")
        name = first.strip()
        left, right = second.split(",")
        left = "".join((char for char in left if char.isalpha()))
        right = "".join((char for char in right if char.isalpha()))
        
        network[name] = (left, right)
        
    return Map(instructions, network)

def main():
    lines = []
    with open("input.txt") as in_file:
        lines = in_file.readlines()
    map = parse_input(lines)
    print(map)

    answer1 = solve1(map)
    answer2 = solve2(map)

    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")


if __name__ == "__main__":
    main()