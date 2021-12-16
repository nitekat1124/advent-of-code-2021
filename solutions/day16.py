import math
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
        BITS = "".join(bin(int(i, 16))[2:].rjust(4, "0") for i in data[0])
        *v, _ = self.parse_bits(BITS)
        r = self.get_value(v, "version")
        return r

    def part2(self, data):
        BITS = "".join(bin(int(i, 16))[2:].rjust(4, "0") for i in data[0])
        *v, _ = self.parse_bits(BITS)
        r = self.get_value(v)
        return r

    def parse_bits(self, BITS):
        ver = int(BITS[:3], 2)
        BITS = BITS[3:]

        type_id = int(BITS[:3], 2)
        BITS = BITS[3:]

        if type_id == 4:
            values = [BITS[:5]]
            idx = 5
            while values[-1][0] == "1":
                values += [BITS[idx : (idx := idx + 5)]]
            BITS = BITS[idx:]
            values = int("".join([v[1:] for v in values]), 2)
        else:
            length_type_id = BITS[:1]
            BITS = BITS[1:]
            if length_type_id == "0":
                length = int(BITS[:15], 2)
                BITS = BITS[15:]
                sub_packets = BITS[:length]
                BITS = BITS[length:]

                values = []
                while len(sub_packets):
                    *value, sub_packets = self.parse_bits(sub_packets)
                    values += [value]
            else:
                length = int(BITS[:11], 2)
                BITS = BITS[11:]
                values = []
                for _ in range(length):
                    *value, BITS = self.parse_bits(BITS)
                    values += [value]

        return [ver, type_id, values, BITS]

    def get_value(self, v, get_type="value"):
        ver = v[0]
        type_id = v[1]
        values = v[2]

        get_version = get_type == "version"

        if type_id == 0:
            return ver + sum([self.get_value(v, "version") for v in values]) if get_version else sum([self.get_value(v) for v in values])
        elif type_id == 1:
            return ver + sum([self.get_value(v, "version") for v in values]) if get_version else math.prod([self.get_value(v) for v in values])
        elif type_id == 2:
            return ver + sum([self.get_value(v, "version") for v in values]) if get_version else min([self.get_value(v) for v in values])
        elif type_id == 3:
            return ver + sum([self.get_value(v, "version") for v in values]) if get_version else max([self.get_value(v) for v in values])
        elif type_id == 4:
            return ver if get_version else values
        elif type_id == 5:
            return ver + sum([self.get_value(v, "version") for v in values]) if get_version else [0, 1][self.get_value(values[0]) > self.get_value(values[1])]
        elif type_id == 6:
            return ver + sum([self.get_value(v, "version") for v in values]) if get_version else [0, 1][self.get_value(values[0]) < self.get_value(values[1])]
        elif type_id == 7:
            return ver + sum([self.get_value(v, "version") for v in values]) if get_version else [0, 1][self.get_value(values[0]) == self.get_value(values[1])]
