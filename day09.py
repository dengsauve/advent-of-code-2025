from input import day_09_test, day_09

def part1(input):
    largest_area = 0
    for c1 in input:
        for c2 in input:
            x = c2[0] - c1[0] + 1
            y = c2[1] - c1[1] + 1
            if x * y > largest_area:
                largest_area = x * y
    return largest_area



def part2():
    pass


def main():
    test_input = day_09_test.split("\n")
    test_input = [[int(s.split(",")[0]), int(s.split(",")[1])] for s in test_input]
    challenge_input = day_09.split("\n")
    challenge_input = [[int(s.split(",")[0]), int(s.split(",")[1])] for s in challenge_input]

    print("=== Test Input ===")

    total = part1(test_input)
    print(f"Part 1: {total}")
    assert total == 50

    # total = part2(test_input)
    # print(f"Part 2: {total}")
    # assert total == 40

    print(f"\n=== Challenge Input: ===")
    total = part1(challenge_input)
    print(f"Part 1: {total}")

    # total = part2(challenge_input)
    # print(f"Part 2: {total}")

if __name__ == "__main__":
    main()