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
        data = [*map(int, data[0].split(","))]
        return self.fish_count(data, 80)

    def part2(self, data):
        data = [*map(int, data[0].split(","))]
        return self.fish_count(data, 256)

    def fish_count(self, data, days):
        """this method is ok in part 1, but really slow in part 2"""
        # for _ in range(days):
        #     n = data.count(0)
        #     data = [i - 1 if i > 0 else 6 for i in data]
        #     data += [8] * n
        # return len(data)

        fish = [0] * 7
        fish_new = [0] * 9

        for i in data:
            fish[i] += 1

        for i in range(days):
            x = fish[0] + fish_new[0]
            fish = fish[1:] + [x]
            fish_new = fish_new[1:] + [x]

        return sum(fish) + sum(fish_new)
