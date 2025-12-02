from input import day_01

# input = day_01.split("\n")
input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".split("\n")

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

# part 2
pointer = 50
password_counter = 0

for turn in input:
    instructions = (turn[0], turn[1:])
    
    if instructions[0] == "L":
        if (pointer - int(instructions[1])) <= 0:
            password_counter += abs(int((pointer - int(instructions[1])) / 100))
        pointer -= int(instructions[1])
    else:
        if (pointer + int(instructions[1])) >= 99:
            password_counter += int((pointer + int(instructions[1])) / 100)
        pointer += int(instructions[1])

    pointer = pointer % 100
    
    if pointer == 0:
        password_counter += 1

print(f"Part 2: {password_counter}")
# 2466 is too low
# 5954 is too high lol