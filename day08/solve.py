from itertools import cycle
import math

class Map:

    def __init__(self, instructions, network) -> None:
        self.instructions = instructions
        self.network = network
        
        self._instr_iter = cycle(self.instructions)
        self._current_node = "AAA"
    
    def set_starting_node(self, node: str):
        self._current_node = node

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


# The idea here is to find the length of the repeating loop
# for each path, and then find the least common multiple
# of each length to find the shortest number of steps
# for them all to end on Z.
# I don't think this always works, but it does if the path from start to
# finish always loops equally, which seems to be true based on trial and error.
def solve2(map: Map) -> int:
    starting_nodes = []
    for node in map.network.keys():
        if node.endswith("A"):
            starting_nodes.append(node)
    print(starting_nodes)
    
    distances = []

    for node in starting_nodes:
        map.set_starting_node(node)
        counter = 1
        while map.next()[2] != "Z":
            counter += 1
        distances.append(counter)
    
    print(distances)
    
    return math.lcm(*distances)

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
        left = "".join((char for char in left if char.isalnum()))
        right = "".join((char for char in right if char.isalnum()))
        
        network[name] = (left, right)
        
    return Map(instructions, network)

def main():
    lines = []
    with open("input.txt") as in_file:
        lines = in_file.readlines()
    map = parse_input(lines)

    answer1 = solve1(map)
    answer2 = solve2(map)

    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")


if __name__ == "__main__":
    main()