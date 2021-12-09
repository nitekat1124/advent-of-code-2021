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

    def part2_alt(self, data):
        # for signals a to g, pre-calculate how many times they will be turn on through 0 to 9
        # ex: signal a will be turn on 8 times, and signal b will be turn on 6 times...
        # and for 0 to 9, add all their turned-on signals counts together
        # ex: number 7 will turn on signals [a, c, f], since a had count 8 times, c had count 8 times and f had count 9 times, so number 7 has a total count as 8+8+9=25
        count_mapping = [42, 17, 34, 39, 30, 37, 41, 25, 49, 45]
        return sum(int("".join(str(count_mapping.index(sum(line.split("|")[0].count(val) for val in values))) for values in line.split("|")[1].strip().split())) for line in data)
