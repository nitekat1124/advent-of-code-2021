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
        diagram = {}
        for line in data:
            a, b = [[*map(int, i.split(","))] for i in line.split(" -> ")]
            x = sorted([a[0], b[0]])
            y = sorted([a[1], b[1]])
            X = Y = None

            if len(set(x)) == 1:
                Y = [*range(y[0], y[1] + 1)]
                X = [x[0]] * len(Y)
            elif len(set(y)) == 1:
                X = [*range(x[0], x[1] + 1)]
                Y = [y[0]] * len(X)

            if X and Y:
                for p, q in zip(X, Y):
                    key = p * 1000 + q
                    diagram[key] = diagram.get(key, 0) + 1

        return len([i for i in diagram.values() if i > 1])

    def part2(self, data):
        diagram = {}
        for line in data:
            a, b = [[*map(int, i.split(","))] for i in line.split(" -> ")]
            x = sorted([a[0], b[0]])
            y = sorted([a[1], b[1]])
            X = Y = None

            if len(set(x)) == 1:
                Y = [*range(y[0], y[1] + 1)]
                X = [x[0]] * len(Y)
            elif len(set(y)) == 1:
                X = [*range(x[0], x[1] + 1)]
                Y = [y[0]] * len(X)
            elif x[1] - x[0] == y[1] - y[0]:
                s = 1 if b[0] > a[0] else -1
                t = 1 if b[1] > a[1] else -1
                X = [*range(a[0], b[0] + s, s)]
                Y = [*range(a[1], b[1] + t, t)]

            if X and Y:
                for p, q in zip(X, Y):
                    key = p * 1000 + q
                    diagram[key] = diagram.get(key, 0) + 1

        return len([i for i in diagram.values() if i > 1])
