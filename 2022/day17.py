import datautils

_horizontal_line = [int('0011110', 2)]

_plus = [int('0001000', 2),
         int('0011100', 2),
         int('0001000', 2)]

_corner = [int('0011100', 2),
           int('0000100', 2),
           int('0000100', 2)]

_vertical_line = [int('0010000', 2),
                  int('0010000', 2),
                  int('0010000', 2),
                  int('0010000', 2)]

_square = [int('0011000', 2),
           int('0011000', 2)]

_rocks = [_horizontal_line, _plus, _corner, _vertical_line, _square]


class Simulation:
    def __init__(self, jets):
        self.jets = jets
        self.stopped = [int('1111111', 2)]  # floor
        self.jet_idx = 0
        self.rock_idx = 0
        self.highest = 0
        self.states = {}

    def _find_depth(self):
        depths = []
        for idx in range(0, 7):
            for depth, line in enumerate(reversed(self.stopped[:self.highest+1])):
                if line >> 7-1-idx & 1 == 1:
                    depths.append(-depth)
                    break
        return tuple(depths)

    def _move(self, rock, existing):
        if self.jets[self.jet_idx] == '>':
            wall_collision = any([line & 1 > 0 for line in rock])
            rock_collision = any([line >> 1 & existing[idx] > 0 for idx, line in enumerate(rock)])
            if wall_collision or rock_collision:
                return rock
            else:
                return [line >> 1 for line in rock]
        elif self.jets[self.jet_idx] == '<':
            wall_collision = any([line & 1000000 > 0 for line in rock])
            rock_collision = any([(line << 1) & existing[idx] > 0 for idx, line in enumerate(rock)])
            if wall_collision or rock_collision:
                return rock
            else:
                return [line << 1 for line in rock]

    @staticmethod
    def _can_drop(rock, existing):
        return all([line & existing[idx] == 0 for idx, line in enumerate(rock)])

    def step_n(self, n):
        skipped = 0
        i = 0
        while i < n:
            self._step()

            state = (self.rock_idx, self.jet_idx, self._find_depth())

            if state in self.states:
                (old_i, old_highest) = self.states[state]
                repeat = (n - i) // (i - old_i)
                skipped += (self.highest - old_highest) * repeat
                self.states[state] = ((i - old_i) * repeat, self.highest)
                i += (i - old_i) * repeat + 1
                self.states = {}
            else:
                self.states[state] = (i, self.highest)
                i += 1

        return self.highest + skipped

    def _step(self):
        current = _rocks[self.rock_idx]
        offset_min = self.highest + 4

        if len(self.stopped) < offset_min + len(current):
            for _ in range(len(self.stopped), offset_min + len(current)):
                self.stopped.append(int('0000000', 2))

        movable = True
        while movable:
            current = self._move(current, self.stopped[offset_min:(offset_min + len(current))])
            movable = Simulation._can_drop(current, self.stopped[(offset_min - 1):(offset_min - 1 + len(current))])
            if movable:
                offset_min -= 1

            self.jet_idx = (self.jet_idx + 1) % len(self.jets)

        for idx, line in enumerate(current):
            self.stopped[idx+offset_min] |= line

        self.highest = max(self.highest, len(current) + offset_min - 1)
        self.rock_idx = (self.rock_idx + 1) % len(_rocks)
        return


def pt1(jets):
    sim = Simulation(jets)
    return sim.step_n(2022)


def pt2(jets):
    sim = Simulation(jets)
    return sim.step_n(1000000000000)


def parse_input(data):
    return [*data]


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/17/input"
    input_data = datautils.read_input_data(url)
    parsed = parse_input(input_data)

    print("({},  {})".format(pt1(parsed), pt2(parsed)))
