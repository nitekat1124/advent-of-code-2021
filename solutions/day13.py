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

    """
    # original
    def parse_data(self, data):
        sep = data.index("")

        pos = [[*map(int, i.split(","))] for i in data[:sep]]
        w = max([i[0] for i in pos]) + 1
        h = max([i[1] for i in pos]) + 1

        paper = [list("." * w) for _ in range(h)]

        for i in pos:
            paper[i[1]][i[0]] = "#"

        instructions = [[(x := i.split()[2].split("="))[0], int(x[1])] for i in data[sep + 1 :]]

        return paper, instructions

    def fold(self, paper, instructions):
        for inst in instructions:
            if inst[0] == "y":
                parts = [paper[: inst[1]], paper[inst[1] + 1 :][::-1]]

                h = max(map(len, parts))
                w = len(parts[0][0])

                for i, p in enumerate(parts):
                    if len(p) < h:
                        parts[i] = [list("." * w) for _ in range(h - len(p))] + p
            else:
                parts = [[i[: inst[1]] for i in paper], [i[inst[1] + 1 :][::-1] for i in paper]]

                w = max([len(parts[0][0]), len(parts[1][0])])
                h = len(parts[0])

                for i, p in enumerate(parts):
                    if len(p[0]) < w:
                        parts[i] = [list("".join(line).rjust(w, ".")) for line in p]

            paper = [["#" if "#" in [x[i], y[i]] else "." for i in range(w)] for x, y in zip(*parts)]
        return paper

    def part1(self, data):
        paper, instructions = self.parse_data(data)
        paper = self.fold(paper, instructions[:1])
        return sum(i.count("#") for i in paper)

    def part2(self, data):
        paper, instructions = self.parse_data(data)
        paper = self.fold(paper, instructions)
        for i in paper:
            print(*["#" if c == "#" else " " for c in i], sep="")
        print()
        return 0
    """

    # improved
    def parse_data(self, data):
        sep = data.index("")
        dots = [(*map(int, i.split(",")),) for i in data[:sep]]
        instructions = [[(x := i.split()[2].split("="))[0], int(x[1])] for i in data[sep + 1 :]]
        return dots, instructions

    def fold(self, dots, instructions):
        for inst in instructions:
            w = max(i[0] for i in dots)
            h = max(i[1] for i in dots)
            inst_type = int(inst[0] == "y")
            leng = [w, h][inst_type]
            padding = inst[1] * 2 - leng
            fold_after_half = leng / 2 < inst[1]
            for i, v in enumerate(dots):
                x, y = v
                p = [x, y][inst_type]
                p = [[padding + p, leng - p], [p, 2 * inst[1] - p]][fold_after_half][p > inst[1]]
                dots[i] = [(p, y), (x, p)][inst_type]
        return [*set(dots)]

    def part1(self, data):
        dots, instructions = self.parse_data(data)
        dots = self.fold(dots, instructions[:1])
        return len(dots)

    def part2(self, data):
        dots, instructions = self.parse_data(data)
        dots = self.fold(dots, instructions)
        w = max(i[0] for i in dots) + 1
        h = max(i[1] for i in dots) + 1
        print(*["".join("#" if (i, j) in dots else " " for i in range(w)) for j in range(h)], sep="\n")
