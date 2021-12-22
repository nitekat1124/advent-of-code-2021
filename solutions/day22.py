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
        steps = []
        for line in data:
            r = re.findall(r"^(on|off)\sx\=(.*?)\.\.(.*?),y\=(.*?)\.\.(.*?),z\=(.*?)\.\.(.*?)$", line)[0]
            o = r[0]
            x = [*range(max(-50, int(r[1])), min(50, int(r[2])) + 1)]
            y = [*range(max(-50, int(r[3])), min(50, int(r[4])) + 1)]
            z = [*range(max(-50, int(r[5])), min(50, int(r[6])) + 1)]
            steps += [(o, x, y, z)]

        cube_state = {}
        for o, x, y, z in steps:
            for a in x:
                for b in y:
                    for c in z:
                        cube_state[(a, b, c)] = 1 if o == "on" else 0

        return sum(cube_state.values())

    def part2(self, data):
        steps = []
        for line in data:
            r = re.findall(r"^(on|off)\sx\=(.*?)\.\.(.*?),y\=(.*?)\.\.(.*?),z\=(.*?)\.\.(.*?)$", line)[0]
            o = r[0]
            x = [int(r[1]), int(r[2])]
            y = [int(r[3]), int(r[4])]
            z = [int(r[5]), int(r[6])]
            steps += [(o, x, y, z)]

        on = []
        off = []
        count = 0

        for o, x, y, z in steps:
            on_len = len(on)
            off_len = len(off)

            if o == "on":
                count += (abs(x[1] - x[0]) + 1) * (abs(y[1] - y[0]) + 1) * (abs(z[1] - z[0]) + 1)
                on += [(x, y, z)]

            for i in range(on_len):
                cube = on[i]
                a, b, c = self.intersect((x, y, z), cube)
                if a and b and c:
                    count -= (abs(a[1] - a[0]) + 1) * (abs(b[1] - b[0]) + 1) * (abs(c[1] - c[0]) + 1)
                    off += [(a, b, c)]

            for i in range(off_len):
                cube = off[i]
                a, b, c = self.intersect((x, y, z), cube)
                if a and b and c:
                    count += (abs(a[1] - a[0]) + 1) * (abs(b[1] - b[0]) + 1) * (abs(c[1] - c[0]) + 1)
                    on += [(a, b, c)]
        return count

    def intersect(self, a, b):
        x = sorted(a[0] + b[0])[1:3] if any(i in range(a[0][0], a[0][1] + 1) for i in b[0]) or any(i in range(b[0][0], b[0][1] + 1) for i in a[0]) else []
        y = sorted(a[1] + b[1])[1:3] if any(i in range(a[1][0], a[1][1] + 1) for i in b[1]) or any(i in range(b[1][0], b[1][1] + 1) for i in a[1]) else []
        z = sorted(a[2] + b[2])[1:3] if any(i in range(a[2][0], a[2][1] + 1) for i in b[2]) or any(i in range(b[2][0], b[2][1] + 1) for i in a[2]) else []
        return x, y, z
