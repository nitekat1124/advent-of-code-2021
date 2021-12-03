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
        gam = int("".join(str(int(sum(int(d[i]) for d in data) * 2 > len(data))) for i in range(len(data[0]))), 2)
        eps = 2 ** len(data[0]) - gam - 1

        return gam * eps

    def part2(self, data):
        oxy_data = data
        co2_data = data
        data_len = len(data[0])

        for i in range(data_len):
            oxy_data = [o for o in oxy_data if o[i] == ["0", "1"][sum(int(o[i]) for o in oxy_data) * 2 >= len(oxy_data)]] if len(oxy_data) > 1 else oxy_data
            co2_data = [c for c in co2_data if c[i] == ["1", "0"][sum(int(c[i]) for c in co2_data) * 2 >= len(co2_data)]] if len(co2_data) > 1 else co2_data

        oxy = int(oxy_data[0], 2)
        co2 = int(co2_data[0], 2)

        return oxy * co2
