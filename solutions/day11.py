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
        _map = [*map(int, "".join(data))]
        flashes = 0
        for _ in range(100):
            _map, flash_count = self.get_flashes([energy + 1 for energy in _map])
            flashes += flash_count
        return flashes

    def part2(self, data):
        _map = [*map(int, "".join(data))]
        steps = 0
        while 1:
            _map, _ = self.get_flashes([energy + 1 for energy in _map])
            steps += 1
            if sum(1 for energy in _map if energy == 0) == 100:
                return steps

    def get_flashes(self, _map):
        f = []
        while sum(1 for energy in _map if energy > 9) > len(f):
            for idx, energy in enumerate(_map):
                if energy > 9 and idx not in f:
                    f += [idx]
                    adjs_relative = [[x, y] for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0]
                    adjs_idx = [pos[0] * 10 + pos[1] for pos in [[a[0] + idx // 10, a[1] + idx % 10] for a in adjs_relative] if 10 > pos[0] > -1 and 10 > pos[1] > -1]
                    for p in adjs_idx:
                        _map[p] += 1
        _map = [0 if energy > 9 else energy for energy in _map]
        return _map, len(f)
