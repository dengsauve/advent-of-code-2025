from input import day_02

# input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
input = day_02

def parse_ranges(input):
    range_array = []
    for ranges in input.split(","):
        range_array.append(ranges.split("-"))
    return range_array

ranges = parse_ranges(input)
invalid_ids = []

for r in ranges:
    start = int(r[0])
    end = int(r[1]) + 1 # range method is funny
    check_range = list(range(start, end))
    # print(check_range)
    for num in check_range:
        num_str = str(num)
        if len(num_str) % 2 == 0:
            halfway = int(len(num_str) / 2)
            h1 = num_str[0:halfway]
            h2 = num_str[halfway:]
            if h1 == h2:
                invalid_ids.append(num)

part_1_sum = sum(invalid_ids)
print(f"Part 1: {part_1_sum}")

# Part 2 - longest is 10 digits
#   1s - check for 2, 3, 4, 5, 6, 7, 8, 9, 10 (mirror check), (index & mirror halves check)
#   2s - check for 4, 6, 8, 10 (mirror checks)
#   3s - check for 6, 9
#   4s - check for 8
#   5s - check for 10
# 
#   Mirror Check covers:
#       1s - 2, 4, 6, 8, 10
#       2s - 4, 8
#       3s - 6
#       4s - all
#       5s - all
#
#   Uniq Check covers:
#       1s - 3, 5, 7, 9
#       
#   Edges:
#       2s - 6, 10
#       3s - 9

invalid_ids = []

for r in ranges:
    start = int(r[0])
    end = int(r[1]) + 1 # range method is funny
    check_range = list(range(start, end))
    # print(check_range)
    for num in check_range:
        num_str = str(num)
        # Mirror Check
        if len(num_str) % 2 == 0:
            halfway = int(len(num_str) / 2)
            h1 = num_str[0:halfway]
            h2 = num_str[halfway:]
            if h1 == h2:
                invalid_ids.append(num)
        # Unique Check
        if len(num_str) % 2 == 1 and len(num_str) > 1:
            if len(list(set(num_str))) == 1:
                invalid_ids.append(num)
        # Check 6 long for repeats of 2
        if len(num_str) == 6:
            if num_str[0:2] == num_str[2:4] == num_str[4:6]:
                invalid_ids.append(num)
        # Check 10 long for repeats of 2
        if len(num_str) == 10:
            if num_str[0:2] == num_str[2:4] == num_str[4:6] == num_str[6:8] == num_str[8:10]:
                invalid_ids.append(num)
        # Check 9 long for repeats of 3
        if len(num_str) == 9:
            if num_str[0:3] == num_str[3:6] == num_str[6:9]:
                invalid_ids.append(num)

invalid_ids = list(set(invalid_ids))
part_2_sum = sum(invalid_ids)
print(f"Part 2: {part_2_sum}")