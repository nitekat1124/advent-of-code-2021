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
        algo = data[0]
        _map = data[2:]
        for i in range(2):
            _map = self.enhance(self.pad(_map, [".", algo[0]][i % 2]), algo)
        return "".join(_map).count("#")

    def part2(self, data):
        algo = data[0]
        _map = data[2:]
        for i in range(50):
            _map = self.enhance(self.pad(_map, [".", algo[0]][i % 2]), algo)
        return "".join(_map).count("#")

    def pad(self, _map, p):
        _map = [p * 2 + i + p * 2 for i in _map]
        line = p * len(_map[0])
        return [line] * 2 + _map + [line] * 2

    def enhance(self, _map, algo):
        new_map = [list("." * (len(_map[0]))) for i in range(len(_map))]

        for i in range(1, len(_map) - 1):
            for j in range(1, len(_map[0]) - 1):
                new_map[i][j] = algo[int((_map[i - 1][j - 1 : j + 2] + _map[i][j - 1 : j + 2] + _map[i + 1][j - 1 : j + 2]).replace(".", "0").replace("#", "1"), 2)]
        _map = ["".join(i[1:-1]) for i in new_map[1:-1]]

        return _map
