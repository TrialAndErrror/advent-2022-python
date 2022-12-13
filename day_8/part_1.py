from typing import List


def read_file(file_path):
    with open(file_path, "r") as data:
        return [line.rstrip() for line in data]


def check_against_neighbors(character, blocking_trees):
    return list(filter(lambda x: int(character) <= x, blocking_trees))


class TreeSolver:
    data: List[List[str]]
    total: int = 0

    height: int
    width: int

    def __init__(self, data):
        self.data = data
        self.height = len(self.data)
        self.width = len(self.data[0])

    def check_if_visible(self, character, line_index, character_index):
        if line_index == 0 or character_index == 0 or line_index == self.height or character_index == self.width:
            # Tree is on one of the sides
            return True
        else:
            trees_above = [int(self.data[num][character_index]) for num in range(0, line_index)]
            trees_below = [int(self.data[num][character_index]) for num in range(line_index + 1, self.height)]

            trees_to_left = [int(self.data[line_index][num]) for num in range(0, character_index)]
            trees_to_right = [int(self.data[line_index][num]) for num in range(character_index + 1, self.width)]

            """
            Check each list to see if there are any trees at or above height of current tree;
            if list is empty, then our tree is visible
            """

            check = any([
                len(check_against_neighbors(character, trees_above)) == 0,
                len(check_against_neighbors(character, trees_below)) == 0,
                len(check_against_neighbors(character, trees_to_left)) == 0,
                len(check_against_neighbors(character, trees_to_right)) == 0
            ])

            return check

    def solve(self):
        for line_index, line in enumerate(self.data):
            for character_index, character in enumerate(line):
                is_visible = self.check_if_visible(character, line_index, character_index)
                self.total += int(is_visible)


if __name__ == '__main__':
    obj = TreeSolver(read_file("my_data.txt"))
    obj.solve()
    print(f"Part 1: Total visible trees: {obj.total}")
