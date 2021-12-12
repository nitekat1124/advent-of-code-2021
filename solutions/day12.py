from collections import deque
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
        caves = {}
        for i in data:
            a, b = i.split("-")
            caves[a] = [*set(caves.get(a, []) + [b])]
            caves[b] = [*set(caves.get(b, []) + [a])]
        return self.get_path_count(caves, "start", "end", False)

    def part2(self, data):
        caves = {}
        for i in data:
            a, b = i.split("-")
            caves[a] = [*set(caves.get(a, []) + [b])]
            caves[b] = [*set(caves.get(b, []) + [a])]
        return self.get_path_count(caves, "start", "end", True)

    def get_path_count(self, caves_map, start, end, allow_twice, method=1):
        if method == 3:
            # my original answer, iterative finding all the paths, slow in part 2 even use deque instead of list
            return self.all_path_find(caves_map, start, end, allow_twice)
        elif method == 2:
            # iterative finding the path to the end and counting, like my original answer, but faster
            return self.iterative_find(caves_map, start, end, allow_twice)
        else:
            # recursive finding the path to the end and counting, the fastest
            return self.recursive_find(caves_map, start, set(), allow_twice)

    def recursive_find(self, caves_map, current_cave, seen, allow_twice):
        if current_cave == "end":
            return 1
        path_count = 0
        for next_cave in caves_map[current_cave]:
            if next_cave == "start":
                continue
            elif next_cave.islower():
                if next_cave not in seen:
                    path_count += self.recursive_find(caves_map, next_cave, seen | {next_cave}, allow_twice)
                elif allow_twice:
                    path_count += self.recursive_find(caves_map, next_cave, seen, False)
            else:
                path_count += self.recursive_find(caves_map, next_cave, seen | {next_cave}, allow_twice)
        return path_count

    def iterative_find(self, caves_map, start, end, allow_twice):
        paths = deque([[start, set(), allow_twice]])
        path_count = 0
        while len(paths):
            current_cave, seen, allow_twice = paths.pop()

            if current_cave == end:
                path_count += 1
            else:
                if current_cave.islower():
                    if current_cave not in seen:
                        paths.extend([[next_cave, seen | {current_cave}, allow_twice] for next_cave in caves_map[current_cave] if next_cave != start])
                    elif allow_twice:
                        paths.extend([[next_cave, seen | {current_cave}, False] for next_cave in caves_map[current_cave] if next_cave != start])
                else:
                    paths.extend([[next_cave, seen | {current_cave}, allow_twice] for next_cave in caves_map[current_cave] if next_cave != start])

        return path_count

    def all_path_find(self, caves_map, start, end, allow_twice):
        need_check = deque([[start]])
        paths = deque([])
        while len(need_check) > 0:
            curr = need_check.pop()
            this_allow_twice = allow_twice & (max([curr.count(i) for i in curr if i.islower()]) < 2)
            ns = caves_map[curr[-1]]
            np = [curr + [i] for i in ns if i.isupper() or (i != start and (this_allow_twice or (i not in curr)))]
            need_check.extend(np)
            paths.extend([i for i in need_check if i[-1] == end])
            need_check = deque([i for i in need_check if i[-1] != end])
        return len(paths)
