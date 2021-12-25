from functools import cache
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def solve(self, part_num: int):
        # self.test_runner(part_num)

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
        self.parse_alu(data)
        result = self.guess(0, 0)  # from digit 0, with init z = 0
        return max(int(i) for i in result)

    def part2(self, data):
        self.parse_alu(data)
        result = self.guess(0, 0)
        return min(int(i) for i in result)

    def parse_alu(self, data):
        # ref: puzzle_input_analyze.txt
        # the monad repeat the same pattern for 14 times, the pattern include 18 alu commands
        # and the following 3 type of alu commands/data are all we need
        self.add_x, self.div_z, self.add_y = [], [], []
        for i, line in enumerate(data):
            p = line.split()
            if p[0:2] == ["add", "x"] and p[2] != "z":
                self.add_x += [int(p[2])]
            if p[0:2] == ["div", "z"]:
                self.div_z += [int(p[2])]
            if p[0:2] == ["add", "y"] and i % 18 == 15:
                self.add_y += [int(p[2])]

    @cache
    def guess(self, digit, z):
        models = []
        if digit == len(self.add_x):
            return z == 0
        else:
            # x in this digit, will compare to w
            test_x = self.add_x[digit] + (z % 26)
            # if test_x not in 1 to 9, it won't equal to w, then we have to test all possibilities
            possible_w = [test_x] if 0 < test_x < 10 else [*range(1, 10)]
            for w in possible_w:
                next_z = self.calc_z(digit, w, z)
                res = self.guess(digit + 1, next_z)  # recursive guess every digit
                if res is True:
                    models += [str(w)]
                elif type(res) is list:
                    for following_w in res:
                        models += [str(w) + following_w]
            return models

    def calc_z(self, digit, w, z):
        # ref: puzzle_input_analyze.txt
        x = (z % 26) + self.add_x[digit]
        z //= self.div_z[digit]
        if x != w:
            z = z * 26 + w + self.add_y[digit]
        return z

    """
    def part1(self, data):
        alu = data

        monad = "9" * 14
        while not self.test(monad, alu):
            monad = str(int(monad) - 1)
            while "0" in monad:
                monad = str(int(monad) - 1)

        return monad

    def test(self, monad, alu):
        i = 0
        n = {
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
        }

        for inst in alu:
            inst = inst.split()
            if inst[0] == "inp":
                n[inst[1]] = int(monad[i])
                i += 1
            elif inst[0] == "add":
                v = n[inst[2]] if inst[2].isalpha() else int(inst[2])
                exec(f"n['{inst[1]}'] += v")
            elif inst[0] == "mul":
                v = n[inst[2]] if inst[2].isalpha() else int(inst[2])
                exec(f"n['{inst[1]}'] *= v")
            elif inst[0] == "div":
                v = n[inst[2]] if inst[2].isalpha() else int(inst[2])
                if v != 0:
                    exec(f"n['{inst[1]}'] //= v")
            elif inst[0] == "mod":
                v = n[inst[2]] if inst[2].isalpha() else int(inst[2])
                t = n[inst[1]] >= 0
                s = v >= 0
                if t and s:
                    exec(f"n['{inst[1]}'] %= v")
            elif inst[0] == "eql":
                v = n[inst[2]] if inst[2].isalpha() else int(inst[2])
                exec(f"n['{inst[1]}'] =1 if n['{inst[1]}'] == v else 0")
        return n["z"] == 0
    """
