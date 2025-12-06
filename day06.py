from input import day_06_test, day_06
from helpers import rotate_counter_clockwise, is_int
import math
import re

def part1(input):
    input = [row.split() for row in input]
    input = rotate_counter_clockwise(input)
    total = 0
    for problem in input:
        operator = problem.pop()
        problem = [int(s) for s in problem]
        if operator == "+":
            total += sum(problem)
        elif operator == "*":
            total += math.prod(problem)
    
    return total


def parse_column_lengths(input):
    count = 0
    first = True
    column_lengths = []

    for operator in input[-1].split(" "):
        if operator != "":
            if first:
                first = False
            else:
                column_lengths.append(count)
            count = 1
        elif operator == "":
            count += 1
    column_lengths.append(count) # Cleanup

    return column_lengths


def parse_input_to_grid(input, column_lengths):
    grid = [[] for _ in input]
    start = 0
    for l in column_lengths:
        end = start + l
        for idx, row in enumerate(input):
            target = row[start:end]
            grid[idx].append(target)
        start = end + 1
    
    return grid


def part2(input):
    # Iterate through the last input row, determine column length, and record the max length for each "column"
    column_lengths = parse_column_lengths(input)

    # Using the max length, chunk that length of chars from each row into a new 2d array
    grid = parse_input_to_grid(input, column_lengths)
    print(grid)

    # Rotate the new parsed 2d array
    grid = rotate_counter_clockwise(grid)

    total = 0
    for problem in grid:
        operator = problem.pop().strip()
        ceph_nums = [list(s) for s in problem]
        nums = []
        for i in range(len(ceph_nums[0])):
            num_str = ''
            for num in ceph_nums:
                c = num.pop()
                if c != ' ':
                    num_str += c
            nums.append(num_str)
        nums = [int(n) for n in nums]

        if operator == "+":
            total += sum(nums)
        elif operator == "*":
            total += math.prod(nums)

    return total



def main():
    print("=== Test Input ===")
    input = day_06_test.split("\n")

    total = part1(input)
    print(f"Part 1: {total}")
    assert total == 4277556

    total = part2(input)
    print(f"Part 2: {total}")
    assert total == 3263827

    print(f"\n=== Challenge Input: ===")
    input = day_06.split("\n")

    total = part1(input)
    print(f"Part 1: {total}")

    total = part2(input)
    print(f"Part 2: {total}")


if __name__ == "__main__":
    main()