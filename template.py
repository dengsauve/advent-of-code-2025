from input import day_1_test, day_1
from helpers import multiline_str_to_matrix

def part1(input):
    pass
    

def part2(input):
    pass


def main():
    test_input = ""
    challenge_input = ""
    
    print("=== Test Input ===")

    total = part1(test_input)
    print(f"Part 1: {total}")
    # assert total == 21

    total = part2(test_input)
    print(f"Part 2: {total}")
    # assert total == 40

    print(f"\n=== Challenge Input: ===")

    total = part1(challenge_input)
    print(f"Part 1: {total}")

    total = part2(challenge_input)
    print(f"Part 2: {total}")


if __name__ == "__main__":
    main()