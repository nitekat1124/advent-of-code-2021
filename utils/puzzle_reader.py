import os, sys, glob, re


class PuzzleReader:
    @staticmethod
    def get_puzzle_input(day_num):
        return [line.strip() for line in open(f"{PuzzleReader.get_path()}/data/day{day_num:02d}/puzzle_input.txt", "r").readlines()]

    @staticmethod
    def get_test_input(day_num):
        inputs = []
        for name in sorted(glob.glob(f"{PuzzleReader.get_path()}/data/day{day_num:02d}/*")):
            if len(re.findall(r"^test_\d+_input.txt$", os.path.basename(name))):
                inputs += [[line.strip() for line in open(name, "r").readlines()]]
        return inputs

    @staticmethod
    def get_test_result(day_num, part_num):
        results = []
        for name in sorted(glob.glob(f"{PuzzleReader.get_path()}/data/day{day_num:02d}/*")):
            if len(re.findall(r"^test_\d+_part" + str(part_num) + "_result.txt$", os.path.basename(name))):
                results += [[line.strip() for line in open(name, "r").readlines()]]
        return results

    @staticmethod
    def get_path():
        return path if os.path.isdir(path := os.path.realpath(sys.argv[0])) else os.path.dirname(path)
