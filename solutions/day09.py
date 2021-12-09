import math
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
        caves_map, low = self.get_low_points(data)
        return sum([caves_map[p[0]][p[1]] for p in low]) + len(low)

    def part2(self, data):
        caves_map, low = self.get_low_points(data)

        w = len(caves_map[0])
        h = len(caves_map)

        basins = []

        for i, j in low:
            point = caves_map[i][j]
            if point != 9:
                need_check = [[i, j]]
                checked = []
                while len(need_check) > 0:
                    x = need_check[0]
                    need_check = need_check[1:]

                    adjacents_pos = [p for p in [[x[0] - 1, x[1]], [x[0] + 1, x[1]], [x[0], x[1] - 1], [x[0], x[1] + 1]] if h > p[0] > -1 and w > p[1] > -1]
                    adjacents = [p for p in adjacents_pos if caves_map[p[0]][p[1]] != 9]
                    need_check += adjacents

                    caves_map[x[0]][x[1]] = 9
                    checked += [f"{x[0]}_{x[1]}"]
                basins += [len(set(checked))]

        return math.prod(sorted(basins, reverse=True)[:3])

    def get_low_points(self, data):
        caves_map = [[*map(int, i)] for i in data]
        w = len(caves_map[0])
        h = len(caves_map)
        low = []
        for i in range(h):
            for j in range(w):
                point = caves_map[i][j]
                adjacents_pos = [p for p in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]] if h > p[0] > -1 and w > p[1] > -1]
                adjacents = [caves_map[p[0]][p[1]] for p in adjacents_pos]
                low_adjacents_count = sum([1 for i in adjacents if i <= point])
                if low_adjacents_count == 0:
                    low += [[i, j]]
        return caves_map, low
