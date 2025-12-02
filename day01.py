from input import day_01

input = day_01.split("\n")

dial = list(range(100))
pointer = 50
password_counter = 0

# part 1
for turn in input:
    instructions = (turn[0], turn[1:])
    if instructions[0] == "L":
        pointer -= int(instructions[1])
        pointer = pointer % 100
    else:
        pointer += int(instructions[1])
        pointer = pointer % 100
    if pointer == 0:
        password_counter += 1

print(f"Part 1: {password_counter}")

pointer = 50
password_counter = 0