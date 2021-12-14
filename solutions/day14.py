from collections import Counter
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
                    print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        return self.loop(data, 10)

    def part2(self, data):
        return self.loop(data, 40)

    """
    def loop(self, data, times):
        polymer = data[0]
        rules = {(a := i.split(" -> "))[0]: a[1] for i in data[2:]}

        pairs = {a + b: polymer.count(a + b) for a, b in zip(polymer, polymer[1:])}

        for _ in range(times):
            temp = {}
            for k, v in pairs.items():
                if k in rules:
                    k1 = k[0] + rules[k]
                    k2 = rules[k] + k[1]
                    temp[k] = temp.get(k, 0) - v
                    temp[k1] = temp.get(k1, 0) + v
                    temp[k2] = temp.get(k2, 0) + v

            for k, v in temp.items():
                pairs[k] = pairs.get(k, 0) + v

        c = {}
        for k, v in pairs.items():
            c[k[0]] = c.get(k[0], 0) + v
            c[k[1]] = c.get(k[1], 0) + v
        c[polymer[0]] = c.get(polymer[0], 0) + 1
        c[polymer[-1]] = c.get(polymer[-1], 0) + 1

        return (max(c.values()) - min(c.values())) // 2
    """

    # more easier when use collections.Counter or defaultdict, but Counter is better when create pairs
    def loop(self, data, times):
        polymer = data[0]
        rules = {(a := i.split(" -> "))[0]: a[1] for i in data[2:]}

        pairs = Counter([a + b for a, b in zip(polymer, polymer[1:])])

        for _ in range(times):
            temp = Counter()
            for k, v in pairs.items():
                if k in rules:
                    k1 = k[0] + rules[k]
                    k2 = rules[k] + k[1]
                    temp[k] -= v
                    temp[k1] += v
                    temp[k2] += v

            pairs += temp

        c = Counter()
        for k, v in pairs.items():
            c[k[0]] += v
            c[k[1]] += v
        c[polymer[0]] += 1
        c[polymer[-1]] += 1

        return (max(c.values()) - min(c.values())) // 2
