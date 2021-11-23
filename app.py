import argparse, importlib


def main():
    parser = argparse.ArgumentParser(description="Advent of Code solution runner")
    parser.add_argument("-d", "--day", dest="day", required=True, default=1, metavar="day_number", type=int, help="Required, day number of the AoC event")
    parser.add_argument("-p", "--part ", dest="part", required=True, default=1, metavar="part_number", type=int, help="Required, part number of the day of the AoC event")
    args = parser.parse_args()

    if not 0 < args.day < 26:
        print("day number must be between 1 and 25")
        exit()
    elif args.part not in [1, 2]:
        print("part number must be 1 or 2")
        exit()
    else:
        print(f"Solving day {args.day} part {args.part}\n")
        sol = importlib.import_module(f"solutions.day{args.day:02d}").Solution(args.day)
        print("the answer is", sol.solve(part_num=args.part))


if __name__ == "__main__":
    main()
