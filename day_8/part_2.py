from typing import List

from day_8.part_1 import read_file


class TreeVisibiltyCalc:
    data: List[List[str]]
    height: int
    width: int

    def __init__(self, data):
        self.data = data
        self.height = len(self.data)
        self.width = len(self.data[0])

    def check_if_visible(self, character, line_index, character_index):
        if line_index == 0 or character_index == 0 or line_index == self.height or character_index == self.width:
            # Tree is on one of the sides; will multiply 0 times our score, so it is zero
            return 0
        else:
            character_value = int(character)
            trees_above = [int(self.data[num][character_index]) for num in range(0, line_index)]
            trees_above.reverse()
            trees_below = [int(self.data[num][character_index]) for num in range(line_index + 1, self.height)]

            trees_to_left = [int(self.data[line_index][num]) for num in range(0, character_index)]
            trees_to_left.reverse()
            trees_to_right = [int(self.data[line_index][num]) for num in range(character_index + 1, self.width)]

            """
            Check each list to see if there are any trees at or above height of current tree;
            if list is empty, then our tree is visible
            """

            vision_above = check_vision_distance(character_value, trees_above)
            vision_below = check_vision_distance(character_value, trees_below)
            vision_to_left = check_vision_distance(character_value, trees_to_left)
            vision_to_right = check_vision_distance(character_value, trees_to_right)

            result = (
                    vision_above
                    * vision_below
                    * vision_to_left
                    * vision_to_right
            )

            return result

    def solve(self):
        all_vision_scores = [
            self.check_if_visible(character, line_index, character_index)
            for line_index, line in enumerate(self.data)
            for character_index, character in enumerate(line)
        ]

        return max(all_vision_scores)


def check_vision_distance(character, trees_in_line):
    for num in trees_in_line:
        if num >= character:
            return trees_in_line.index(num) + 1
    return len(trees_in_line)


if __name__ == '__main__':
    obj = TreeVisibiltyCalc(read_file("my_data.txt"))
    score = obj.solve()
    print(f"Part 2: Total visibility score: {score}")
