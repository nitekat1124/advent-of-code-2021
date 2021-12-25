from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def solve(self, part_num: int):
        # self.test_runner(part_num)

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
        """
        #############
        #...........#
        ###B#B#C#D###
          #D#C#A#A#
          #########

        #############
        #.......D...#   D: 2 steps (2000)
        ###B#B#C#.###
          #D#C#A#A#
          #########

        #############
        #.......D.A.#   A: 3 steps (3)
        ###B#B#C#.###
          #D#C#A#.#
          #########

        #############
        #.........A.#   D: 3 steps (3000)
        ###B#B#C#.###
          #D#C#A#D#
          #########

        #############
        #.......C.A.#   C: 2 steps (200)
        ###B#B#.#.###
          #D#C#A#D#
          #########

        #############
        #.A.....C.A.#   A: 8 steps (7)
        ###B#B#.#.###
          #D#C#.#D#
          #########

        #############
        #.A.......A.#   C: 3 steps (300)
        ###B#B#.#.###
          #D#C#C#D#
          #########

        #############
        #.A.B.....A.#   B: 2 steps (20)
        ###B#.#.#.###
          #D#C#C#D#
          #########

        #############
        #A..B.....A.#   C: 5 steps (500)
        ###B#.#C#.###
          #D#.#C#D#
          #########

        #############
        #.A.......A.#   B: 3 steps (30)
        ###B#.#C#.###
          #D#B#C#D#
          #########

        #############
        #.A.......A.#   B: 4 steps (40)
        ###.#B#C#.###
          #D#B#C#D#
          #########

        #############
        #.A.......A.#   D: 9 steps (9000)
        ###.#B#C#D###
          #.#B#C#D#
          #########

        #############
        #.........A.#   A: 4 steps (3)
        ###.#B#C#D###
          #A#B#C#D#
          #########

        #############
        #...........#   A: 8 steps (8)
        ###A#B#C#D###
          #A#B#C#D#
          #########

        2000 + 3 + 3000 + 200 + 7 + 300 + 20 + 500 + 30 + 40 + 9000 + 3 + 8 = 15111
        """

        return 15111

    def part2(self, data):
        """
        #############
        #...........#
        ###B#B#C#D###
          #D#C#B#A#
          #D#B#A#C#
          #D#C#A#A#
          #########

        #############
        #..........B#   B: 7 steps (70)
        ###B#.#C#D###
          #D#C#B#A#
          #D#B#A#C#
          #D#C#A#A#
          #########

        #############
        #.........CB#   C: 4 steps (400)
        ###B#.#.#D###
          #D#C#B#A#
          #D#B#A#C#
          #D#C#A#A#
          #########

        #############
        #.......B.CB#   B: 3 steps (30)
        ###B#.#.#D###
          #D#C#.#A#
          #D#B#A#C#
          #D#C#A#A#
          #########

        #############
        #A......B.CB#   A: 9 steps (9)
        ###B#.#.#D###
          #D#C#.#A#
          #D#B#.#C#
          #D#C#A#A#
          #########

        #############
        #AA.....B.CB#   A: 9 steps (9)
        ###B#.#.#D###
          #D#C#.#A#
          #D#B#.#C#
          #D#C#.#A#
          #########

        #############
        #AA.....B.CB#   C: 8 steps (800)
        ###B#.#.#D###
          #D#.#.#A#
          #D#B#.#C#
          #D#C#C#A#
          #########

        #############
        #AA.B...B.CB#   B: 4 steps (40)
        ###B#.#.#D###
          #D#.#.#A#
          #D#.#.#C#
          #D#C#C#A#
          #########

        #############
        #AA.B...B.CB#   C: 9 steps (900)
        ###B#.#.#D###
          #D#.#.#A#
          #D#.#C#C#
          #D#.#C#A#
          #########

        #############
        #AA.....B.CB#   B: 5 steps (50)
        ###B#.#.#D###
          #D#.#.#A#
          #D#.#C#C#
          #D#B#C#A#
          #########

        #############
        #AA.......CB#   B: 6 steps (60)
        ###B#.#.#D###
          #D#.#.#A#
          #D#B#C#C#
          #D#B#C#A#
          #########

        #############
        #AA.......CB#   B: 5 steps (50)
        ###.#.#.#D###
          #D#B#.#A#
          #D#B#C#C#
          #D#B#C#A#
          #########

        #############
        #AA........B#   C: 5 steps (500)
        ###.#.#.#D###
          #D#B#C#A#
          #D#B#C#C#
          #D#B#C#A#
          #########

        #############
        #AA.........#   B: 7 steps (70)
        ###.#B#.#D###
          #D#B#C#A#
          #D#B#C#C#
          #D#B#C#A#
          #########

        #############
        #AA...D.....#   D: 4 steps (4000)
        ###.#B#.#.###
          #D#B#C#A#
          #D#B#C#C#
          #D#B#C#A#
          #########

        #############
        #AA...D....A#   A: 4 steps (4)
        ###.#B#.#.###
          #D#B#C#.#
          #D#B#C#C#
          #D#B#C#A#
          #########

        #############
        #AA...D....A#   C: 6 steps (600)
        ###.#B#C#.###
          #D#B#C#.#
          #D#B#C#.#
          #D#B#C#A#
          #########

        #############
        #AA...D...AA#   A: 5 steps (5)
        ###.#B#C#.###
          #D#B#C#.#
          #D#B#C#.#
          #D#B#C#.#
          #########

        #############
        #AA.......AA#   D: 7 steps (7000)
        ###.#B#C#.###
          #D#B#C#.#
          #D#B#C#.#
          #D#B#C#D#
          #########

        #############
        #AA.......AA#   D: 11 steps (11000)
        ###.#B#C#.###
          #.#B#C#.#
          #D#B#C#D#
          #D#B#C#D#
          #########

        #############
        #AA.......AA#   D: 11 steps (11000)
        ###.#B#C#.###
          #.#B#C#D#
          #.#B#C#D#
          #D#B#C#D#
          #########

        #############
        #AA.......AA#   D: 11 steps (11000)
        ###.#B#C#D###
          #.#B#C#D#
          #.#B#C#D#
          #.#B#C#D#
          #########

        #############
        #A........AA#   A: 5 steps (5)
        ###.#B#C#D###
          #.#B#C#D#
          #.#B#C#D#
          #A#B#C#D#
          #########

        #############
        #.........AA#   A: 5 steps (5)
        ###.#B#C#D###
          #.#B#C#D#
          #A#B#C#D#
          #A#B#C#D#
          #########

        #############
        #..........A#   A: 9 steps (9)
        ###.#B#C#D###
          #A#B#C#D#
          #A#B#C#D#
          #A#B#C#D#
          #########

        #############
        #...........#   A: 9 steps (9)
        ###A#B#C#D###
          #A#B#C#D#
          #A#B#C#D#
          #A#B#C#D#
          #########

        70 + 400 + 30 + 9 + 9 + 800 + 40 + 900 + 50 + 60 + 50 + 500 + 70 + 4000 + 4 + 600 + 5 + 7000 + 11000 + 11000 + 11000 + 5 + 5 + 9 + 9 = 47625
        """
        return 47625
