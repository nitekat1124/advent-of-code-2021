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
        crabs = [int(i) for i in data[0].split(",")]
        return min([sum(abs(target - crab) for crab in crabs) for target in range(min(crabs), max(crabs) + 1)])

    def part2(self, data):
        crabs = [int(i) for i in data[0].split(",")]
        return min([sum((abs(target - crab) + 1) * abs(target - crab) // 2 for crab in crabs) for target in range(min(crabs), max(crabs) + 1)])
