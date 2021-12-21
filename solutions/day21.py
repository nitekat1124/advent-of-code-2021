import functools
from itertools import product
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def solve(self, part_num: int):
        self.test_runner(part_num)

        func = getattr(self, f"part{part_num}")
        result = func(self.data)
        return result

    def test_runner(self, part_num):
        test_inputs = self.get_test_input()
        test_results = self.get_test_result(part_num)
        test_counter = 1

        func = getattr(self, f"part{part_num}")
        for i, r in zip(test_inputs, test_results):
            if len(r):
                if func(i) == int(r[0]):
                    print(f"test {test_counter} passed")
                else:
                    print(func(i))
                    print(r[0])
                    print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        positions = [int(i[-1]) for i in data]
        dice = [*range(1, 101)]
        i = 0
        scores = [0, 0]

        while max(scores) < 1000:
            while len(dice) < (i + 1) * 3:
                dice += [*range(1, 101)]
            d = dice[i * 3 : i * 3 + 3]

            idx = i % 2
            next_pos = (positions[idx] + sum(d) - 1) % 10 + 1
            positions[idx] = next_pos
            scores[idx] += next_pos
            i += 1
        return min(scores) * 3 * i

    def part2(self, data):
        positions = tuple(int(i[-1]) for i in data)
        return max(self.quantum(positions, (0, 0), 0))

    @functools.cache
    def quantum(self, positions, scores, idx):
        win = [0, 0]

        new_positions = list(positions)
        new_scores = list(scores)

        for d1, d2, d3 in product((1, 2, 3), repeat=3):
            new_positions[idx] = (positions[idx] + d1 + d2 + d3 - 1) % 10 + 1
            new_scores[idx] = scores[idx] + new_positions[idx]
            if new_scores[idx] < 21:
                w1, w2 = self.quantum(tuple(new_positions), tuple(new_scores), 1 - idx)
                win[0] += w1
                win[1] += w2
            else:
                win[idx] += 1

        return win[0], win[1]
