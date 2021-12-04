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
        drawn = data[0].split(",")
        boards = [[x.split() for x in i.split("_")] for i in "_".join(data[2:]).split("__")]

        for d in drawn:
            for b in boards:
                for line in b:
                    if d in line:
                        line[line.index(d)] = "x"
                if "xxxxx" in ["".join(i) for i in b + [[line[x] for line in b] for x in range(5)]]:
                    return self.calc(b, d)
        return None

    def part2(self, data):
        drawn = data[0].split(",")
        boards = [[x.split() for x in i.split("_")] for i in "_".join(data[2:]).split("__")]

        scores = [0] * len(boards)
        complete_order = []

        for d in drawn:
            for x, b in enumerate(boards):
                for line in b:
                    if d in line:
                        line[line.index(d)] = "x"
                if "xxxxx" in ["".join(i) for i in b + [[line[x] for line in b] for x in range(5)]]:
                    if x not in complete_order:
                        s = self.calc(b, d)
                        scores[x] = s
                        complete_order += [x]
        return scores[complete_order[-1]]

    def calc(self, b, d):
        return sum(int(i) for i in [x for i in b for x in i] if i != "x") * int(d)
