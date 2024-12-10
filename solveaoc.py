import importlib
import argparse
import subprocess
import sys
from pathlib import Path

def build_command_line_parser():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    subparsers = parser.add_subparsers(help="Specify whether to run or test the solution", dest="action")	

    solve_parser = subparsers.add_parser("run", help="Run the solver")
    solve_parser.add_argument("year", type=int, help="The year of the Advent of Code challenge")
    solve_parser.add_argument("day", type=int, help="The day of the Advent of Code challenge")
    solve_parser.add_argument("part", type=int, help="The part of the day's challenge (e.g., 1 for part 1, 2 for part 2)")

    test_parser = subparsers.add_parser("test", help="Test the solver")
    test_parser.add_argument("year", type=int, help="The year of the Advent of Code challenge")
    test_parser.add_argument("day", type=int, help="The day of the Advent of Code challenge")

    return parser  


def test_solution(year, day):
    try:
        test_file = f"aoc/year_{year}/day_{day:02d}/test_day_{day:02d}.py"
        # root_dir = Path(__file__).parent
        # subprocess.run(["pytest", "-s", f"--rootdir={root_dir.absolute()}","-m", test_file])
        subprocess.run(["pytest", "-s", test_file])
    except FileNotFoundError:
        print(f"Test file for year {year}, day {day} not found.")


def solve_advent_problem(year, day, part):
    try:
        module_name = f"aoc.year_{year}.day_{day:02d}.part{part}"
        print(module_name)
        module = importlib.import_module(module_name)
        module.solve()
    except ModuleNotFoundError:
        print(f"Solution for year {year}, day {day}, part {part} not found.")
    except AttributeError:
        print(f"Module {module_name} does not have a solve function.")


def main():
    parser = build_command_line_parser()    
    args = parser.parse_args()
    
    if args.action == "run":
        solve_advent_problem(args.year, args.day, args.part)
    elif args.action == "test":
        test_solution(args.year, args.day)
    else:
        parser.print_help() 


if __name__ == "__main__":
    main()