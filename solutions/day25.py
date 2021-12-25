from copy import deepcopy
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
        _map = [list(i) for i in data]
        w = len(data[0])
        h = len(data)
        i = 0

        while 1:
            i += 1
            temp_map2 = deepcopy(_map)

            for y in range(h):
                for x in range(w):
                    if _map[y][x] == ">":
                        x2 = 0 if (x2 := x + 1) == w else x2
                        if _map[y][x2] == ".":
                            temp_map2[y][x2] = ">"
                            temp_map2[y][x] = "."

            temp_map3 = deepcopy(temp_map2)

            for y in range(h):
                for x in range(w):
                    if temp_map2[y][x] == "v":
                        y2 = 0 if (y2 := y + 1) == h else y2
                        if temp_map2[y2][x] == ".":
                            temp_map3[y2][x] = "v"
                            temp_map3[y][x] = "."

            if _map == temp_map3:
                break
            else:
                _map = temp_map3

        return i

    def part2(self, data):
        return "Merry Christmas!"
