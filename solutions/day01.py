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
        data = [*map(int, data)]
        c = sum(1 for i in range(1, len(data)) if data[i] > data[i - 1])
        return c

    def part2(self, data):
        data = [*map(int, data)]
        c = sum(1 for i in range(1, len(data) - 2) if sum(data[i : i + 3]) > sum(data[i - 1 : i + 2]))
        return c
