import re
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
        addition = data[0]
        for i in data[1:]:
            addition = f"[{addition},{i}]"
            while (t := self.reduction(addition)) != addition:
                addition = t
        return self.calc_magnitude(addition)

    def reduction(self, s: str):
        # explode
        depth = 0
        for i, v in enumerate(s):
            if v.isnumeric() and depth > 4:
                pair_close_pos = s[i:].index("]")
                before_pair, pair, after_pair = s[: i - 1], s[i : i + pair_close_pos], s[i + pair_close_pos + 1 :]
                pair = [*map(int, pair.split(","))]

                all_regulars_before_pair = re.findall(r"\d+", before_pair)
                if len(all_regulars_before_pair):
                    reg = all_regulars_before_pair[-1]
                    reg_pos = before_pair.rindex(reg)
                    before_pair = before_pair[:reg_pos] + str(int(reg) + pair[0]) + before_pair[reg_pos + len(reg) :]

                all_regulars_after_pair = re.findall(r"\d+", after_pair)
                if len(all_regulars_after_pair):
                    reg = all_regulars_after_pair[0]
                    reg_pos = after_pair.index(reg)
                    after_pair = after_pair[:reg_pos] + str(int(reg) + pair[1]) + after_pair[reg_pos + len(reg) :]

                return before_pair + "0" + after_pair
            else:
                depth += [1, -1]["[]".index(v)] if v in "[]" else 0

        # split
        large_regulars = [i for i in re.findall(r"\d+", s) if int(i) > 9]
        if len(large_regulars):
            reg = large_regulars[0]
            reg_pos = s.index(reg)

            before_reg, after_reg = s[:reg_pos], s[reg_pos + len(reg) :]
            reg = int(reg)
            elem_left = reg // 2
            elem_right = reg - elem_left
            s = before_reg + f"[{elem_left},{elem_right}]" + after_reg

        return s

    def calc_magnitude(self, s: str):
        while s.count("["):
            pairs = re.findall(r"\[(\d+),(\d+)\]", s)
            for a, b in pairs:
                s = s.replace(f"[{a},{b}]", str(int(a) * 3 + int(b) * 2))
        return int(s)

    def part2(self, data):
        return max(max(self.part1(i), self.part1(i[::-1])) for i in combinations(data, 2))
