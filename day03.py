from input import day03

# input = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111""".split("\n")
input = day03.split("\n")

joltages = []

for bank in input:
    batteries = list(bank)
    highest_value = 0
    second_highest_value = 0
    for battery in batteries[0:-1]:
        if int(battery) > highest_value:
            highest_value = int(battery)
            second_highest_value = 0
        elif int(battery) > second_highest_value:
            second_highest_value = int(battery)
    if int(batteries[-1]) > second_highest_value:
        second_highest_value = int(batteries[-1])
    joltage = int(f"{highest_value}{second_highest_value}")
    joltages.append(joltage)

print(joltages)
print(f"Part 1: {sum(joltages)}")