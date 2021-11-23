import math
from itertools import combinations
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
            if func(i) == int(r[0]):
                print(f"test {test_counter} passed")
            else:
                print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        return self._process(data, entries=2)

    def part2(self, data):
        return self._process(data, entries=3)

    def _process(self, data, entries):
        data = [int(i) for i in data]
        for item in combinations(data, entries):
            if sum(item) == 2020:
                return math.prod(item)
