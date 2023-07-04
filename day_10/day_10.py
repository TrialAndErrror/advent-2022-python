

def parse_command(command_text: str):
    if command_text.strip() == "noop":
        return 0
    elif command_text.startswith("addx"):
        return int(command_text.strip().split(" ")[1])


def get_changes():
    with open("input.txt", "r") as file:
        data = file.readlines()

    return [
        0
        if line.strip() == "noop"
        else int(line.strip().split(" ")[1])
        for line in data
    ]


class ClockCircuit:
    changes: list
    cycles: dict = {}
    change_amounts: list = []

    def __init__(self):
        self.changes = get_changes()
        self.cycles[0] = 1
        self.map_cycles()

    def map_cycles(self):
        for round, change in enumerate(self.changes):
            # Get the number to add from two cycles ago
            num_to_add = 0 if round < 2 else self.change_amounts.pop(0)

            # Determine value during cycle
            self.cycles[round + 1] = self.cycles[round] + num_to_add

            # Figure out number to add after next cycle
            next_change_amount = change if change else 0
            self.change_amounts.append(next_change_amount)

        round = len(self.changes)
        self.cycles[round + 1] = self.cycles[round] + self.change_amounts.pop(0)
        round += 1
        self.cycles[round + 1] = self.cycles[round] + self.change_amounts.pop(0)

        del(self.cycles[0])

    def get_round_charge(self, round):
        final_round = len(self.cycles)
        final_value = self.cycles[final_round]

        if round < final_round:
            return self.cycles[round] * round
        else:
            return final_value * round


if __name__ == '__main__':
    circuit = ClockCircuit()

    total = sum([circuit.get_round_charge(num) for num in [20, 140, 60, 100, 180, 220]])
    print(f'Sum of cycles 20, 140, 60, 180, and 100: {total}')

