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
        return sum(sum(1 for p in line.split("|")[1].strip().split() if len(p) in [2, 3, 4, 7]) for line in data)

    def part2(self, data):
        vals = 0
        for line in data:
            sigs, outs = map(str.strip, line.split("|"))
            sigs = ["".join(sorted(t)) for t in sigs.split()]
            outs = ["".join(sorted(t)) for t in outs.split()]

            mapping = [""] * 10
            lefts = []

            for sig in sigs:
                lines = {2: 1, 4: 4, 3: 7, 7: 8}
                if len(sig) in lines:
                    mapping[lines[len(sig)]] = sig
                else:
                    lefts += [sig]

            for sig in lefts:
                intersections = {5: {3: 2, 5: 3, 4: 5}, 6: {5: 0, 4: 6, 6: 9}}
                idx = intersections[len(sig)][len(set(sig) & set(mapping[1])) + len(set(sig) & set(mapping[4]))]
                mapping[idx] = sig

            vals += int("".join(str(mapping.index(val)) for val in outs))
        return vals
