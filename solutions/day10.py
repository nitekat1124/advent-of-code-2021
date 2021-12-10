import re
from functools import reduce
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
                print(func(i))
                print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        score = 0
        for line in data:
            while len(line_shrink := re.sub(r"\(\)|\[\]|\{\}|\<\>", "", line)) < len(line):
                line = line_shrink
            line = re.sub(r"\(|\[|\{|\<", "", line)
            if len(line):
                score += [3, 57, 1197, 25137][")]}>".index(line[0])]
        return score

    def part2(self, data):
        score = []
        for line in data:
            while len(line_shrink := re.sub(r"\(\)|\[\]|\{\}|\<\>", "", line)) < len(line):
                line = line_shrink
            if len(line) and len(re.sub(r"\(|\[|\{|\<", "", line)) < 1:
                score += [reduce(lambda s, c: s * 5 + " ([{<".index(c), line[::-1], 0)]
        return sorted(score)[len(score) // 2]
