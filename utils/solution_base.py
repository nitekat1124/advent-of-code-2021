from utils.puzzle_reader import PuzzleReader


class SolutionBase:
    def __init__(self, day_num: int = -1):
        self.day_num = day_num
        self.data = PuzzleReader.get_puzzle_input(self.day_num)

    def get_test_input(self):
        return PuzzleReader.get_test_input(self.day_num)

    def get_test_result(self, part_num):
        return PuzzleReader.get_test_result(self.day_num, part_num)
