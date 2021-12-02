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
        x = 0
        y = 0
        for line in data:
            d, X = line.split()
            X = int(X)
            if d == "forward":
                x += X
            else:
                y += {"down": 1, "up": -1}[d] * X
        return x * y

    def part2(self, data):
        x = 0
        y = 0
        aim = 0
        for line in data:
            d, X = line.split()
            X = int(X)
            if d == "forward":
                x += X
                y += X * aim
            else:
                aim += {"down": 1, "up": -1}[d] * X
        return x * y
