from input import day_05, day_05_test

input = day_05_test
input = day_05

def parse_input(input):
    database = input.split("\n\n")
    fresh_ranges = database[0].split("\n")
    ids = database[1].split("\n")
    return fresh_ranges, ids

str_fresh_ranges, ids = parse_input(input)

fresh_ranges = []

for sfr in str_fresh_ranges:
    bounds = sfr.split("-")
    fresh_ranges.append((int(bounds[0]), int(bounds[1])))

fresh_ranges.sort()

print(fresh_ranges)

fresh_ingredients = 0

for i in ids:
    for low, high in fresh_ranges:
        if int(i) >= low and int(i) <= high:
            fresh_ingredients += 1
            break

print(f"Part 1: {fresh_ingredients}")

# Part 2

section_1 = input.strip().split("\n\n")[0].split("\n")
ranges = [tuple(map(int, r.split("-"))) for r in section_1]

ranges.sort()

merged = []
start, end = ranges[0]

for s, e in ranges[1:]:
    if s <= end + 1:
        end = max(end, e)
    else:
        merged.append((start, end))
        start, end = s, e

merged.append((start, end))
total_fresh = sum((e - s + 1) for s, e in merged)

print(f"Part 2: {total_fresh}")