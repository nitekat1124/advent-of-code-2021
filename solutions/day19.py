from collections import defaultdict
from itertools import combinations

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
        scanners = [[tuple(map(int, j.split(","))) for j in i.split("\n")[1:]] for i in "\n".join(data).split("\n\n")]
        _, beacons = self.relocate(scanners)
        return len(beacons)

    def part2(self, data):
        scanners = [[tuple(map(int, j.split(","))) for j in i.split("\n")[1:]] for i in "\n".join(data).split("\n\n")]
        scanners_pos, _ = self.relocate(scanners)
        scanner_pairs = combinations(list(scanners_pos), 2)
        return max(sum(abs(x - y) for x, y in zip(a, b)) for a, b in scanner_pairs)

    def relocate(self, scanners):
        located_beacons = set(scanners[0])
        located_scanner = {(0, 0, 0)}
        scanners = scanners[1:]

        while scanners:
            matched_scanner, matched_scanner_pos, matched_beacons = self.matching(located_beacons, scanners)
            located_beacons |= set(matched_beacons)
            located_scanner.add(matched_scanner_pos)
            scanners.remove(matched_scanner)

        return located_scanner, located_beacons

    def get_all_orientations(self, x, y, z):
        return [
            (x, y, z),
            (-y, x, z),
            (-x, -y, z),
            (y, -x, z),
            (x, -z, y),
            (z, x, y),
            (-x, z, y),
            (-z, -x, y),
            (x, -y, -z),
            (y, x, -z),
            (-x, y, -z),
            (-y, -x, -z),
            (x, z, -y),
            (-z, x, -y),
            (-x, -z, -y),
            (z, -x, -y),
            (-z, y, x),
            (-y, -z, x),
            (z, -y, x),
            (y, z, x),
            (-y, z, -x),
            (-z, -y, -x),
            (y, -z, -x),
            (z, y, -x),
        ]

    def get_all_orient_beacons(self, scanner):
        return [*zip(*[self.get_all_orientations(*p) for p in scanner])]

    def matching(self, located, scanners):
        for scanner in scanners:
            for beacons in self.get_all_orient_beacons(scanner):
                distance_counter = defaultdict(int)
                for b1 in located:
                    for b2 in beacons:
                        distance_counter[tuple([a - b for a, b in zip(b1, b2)])] += 1
                counter_max = sorted(distance_counter.items(), key=lambda i: i[1])[::-1][0]
                if counter_max[1] >= 12:
                    diff = counter_max[0]
                    return scanner, diff, [(x + diff[0], y + diff[1], z + diff[2]) for x, y, z in beacons]
