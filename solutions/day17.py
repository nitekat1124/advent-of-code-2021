import re
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
        targets = re.findall(r"target\sarea\:\sx\=([\-\d]+)..([\-\d]+),\sy\=([\-\d]+)..([\-\d]+)", data[0])
        # range_x = [int(i) for i in targets[0][:2]]
        range_y = [int(i) for i in targets[0][2:]]

        velocity_y = abs(range_y[0])
        return velocity_y * (velocity_y - 1) // 2

    def part2(self, data):
        targets = re.findall(r"target\sarea\:\sx\=([\-\d]+)..([\-\d]+),\sy\=([\-\d]+)..([\-\d]+)", data[0])
        range_x = [int(i) for i in targets[0][:2]]
        range_y = [int(i) for i in targets[0][2:]]

        # stupid implement, maybe improve later
        count = 0

        for velocity_y in range(range_y[0], abs(range_y[0])):
            times = self.get_possible_move_times(velocity_y, range_y)
            possible_x_count = self.get_possible_velocity_x_count(range_x, times)
            count += possible_x_count

        return count

    def get_possible_move_times(self, velocity_y, range_y):
        times = 1
        pos_y = 0
        ret = []

        while 1:
            pos_y += velocity_y
            if range_y[0] <= pos_y <= range_y[1]:
                ret += [times]
            if pos_y < range_y[0]:
                break
            velocity_y -= 1
            times += 1
        return ret

    def get_possible_velocity_x_count(self, range_x, times):
        if len(times) < 1:
            return 0
        ret = 0
        for start_velocity in range(1, range_x[1] + 1):
            count = 0
            pos = 0
            curr_velocity = start_velocity
            for t in range(1, max(times) + 1):
                pos += curr_velocity
                if range_x[0] <= pos <= range_x[1] and (t in times):
                    count += 1
                    break
                curr_velocity = max(0, curr_velocity - 1)
            ret += count
        return ret
