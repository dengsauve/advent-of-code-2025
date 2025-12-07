from input import day_07_test, day_07
from helpers import multiline_str_to_matrix

def part1(input):
    # Iterate through the matrix rows, and apply logic as follows:
    # S: insert a bar directly below S [i + 1][j] = |
    # .: check above space [i - 1][j] for a bar, and set a bar if it exists [i][j] = |
    # ^: check above space [i - 1][j] for a bar, and set a bar to the left and right of the ^ [i][j-1], [i][j+1] = |
    #    AND increment a split counter
    split_counter = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            cell = input[i][j]
            if cell == ".":
                if i > 0:
                    if input[i - 1][j] == "|":
                        input[i][j] = "|"
            elif cell == "^":
                if input[i - 1][j] == "|":
                    if j > 0:
                        input[i][j - 1] = "|"
                    if j < len(input[i]):
                        input[i][j + 1] = "|"
                    split_counter += 1
            elif cell == "S":
                input[i + 1][j] = "|"
        
    return split_counter
    


def part2(input):
    path_counter = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            cell = input[i][j]
            if cell == ".":
                if i > 0:
                    if input[i - 1][j] == "|":
                        input[i][j] = "|"
            elif cell == "^":
                if input[i - 1][j] == "|":
                    if j > 0:
                        input[i][j - 1] = "|"
                        path_counter += 1
                    if j < len(input[i]):
                        input[i][j + 1] = "|"
                        path_counter += 1
            elif cell == "S":
                input[i + 1][j] = "|"
        
    return path_counter


def main():
    test_input = multiline_str_to_matrix(day_07_test)
    challenge_input = multiline_str_to_matrix(day_07)
    print("=== Test Input ===")

    total = part1(test_input)
    print(f"Part 1: {total}")
    assert total == 21

    total = part2(test_input)
    print(f"Part 2: {total}")
    assert total == 40

    print(f"\n=== Challenge Input: ===")
    total = part1(challenge_input)
    print(f"Part 1: {total}")

    # total = part2(challenge_input)
    # print(f"Part 2: {total}")


if __name__ == "__main__":
    main()