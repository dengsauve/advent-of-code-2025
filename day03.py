from input import day_03, day_03_test

def part_1(input):
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
    
    return joltages


def part_2(input):
    joltages = []

    for bank in input:
        batteries = list(bank)
        joltage = []
        start_index = 0
        end_index = len(batteries) - 11
        for i in range(12):
            # Find first highest number in array
            highest_value = '0'
            highest_value_index = 0
            index_counter = 0
            for battery in batteries[start_index:end_index]:
                if battery > highest_value:
                    highest_value = battery
                    highest_value_index = index_counter
                index_counter += 1
            start_index = start_index + 1 + highest_value_index
            end_index += 1
            joltage.append(highest_value)
        
        joltages.append(int(''.join(joltage)))
    
    return joltages


def main():
    # input = day_03_test.split("\n")
    input = day_03.split("\n")
    joltages = part_1(input)
    print(f"Part 1: {sum(joltages)}")
    joltages = part_2(input)
    print(f"Part 2: {sum(joltages)}")


if __name__ == "__main__":
    main()