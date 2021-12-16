import networkx as nx
import heapq
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
        # return self.calc_networkx(data)
        return self.calc_dijkstra_heapq(data)

    def part2(self, data):
        # return self.calc_networkx(data, 5)
        return self.calc_dijkstra_heapq(data, 5)

    def calc_networkx(self, data, size=1):
        risks = [[*map(int, i)] for i in data]
        w = len(data[0])
        h = len(data)

        g = nx.DiGraph()

        for x in range(size * w):
            for y in range(size * h):
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    x2 = x + dx
                    y2 = y + dy
                    if 0 <= x2 < size * w and 0 <= y2 < size * h:
                        g.add_edge((x, y), (x2, y2), risk=(risks[y2 % h][x2 % w] - 1 + x2 // w + y2 // h) % 9 + 1)

        return nx.shortest_path_length(g, (0, 0), (size * w - 1, size * h - 1), weight="risk")

    def calc_dijkstra_heapq(self, data, size=1):
        risks = [[*map(int, i)] for i in data]
        w = len(data[0])
        h = len(data)
        risk_counter = {(0, 0): 0}
        need_checks = [(0, (0, 0))]
        while len(need_checks) > 0:
            risk, (x, y) = heapq.heappop(need_checks)
            if risk <= risk_counter[(x, y)]:
                for pos in [(x + dx, y + dy) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)] if 0 <= x + dx < w * size and 0 <= y + dy < h * size]:
                    pos_risk = risk + ((risks[pos[1] % h][pos[0] % w] - 1 + pos[0] // w + pos[1] // h) % 9 + 1)
                    if pos_risk < risk_counter.get(pos, 2 ** 32):
                        risk_counter[pos] = pos_risk
                        heapq.heappush(need_checks, (pos_risk, pos))

        return risk_counter[(w * size - 1, h * size - 1)]
