from input import day_04, day_04_test

input = day_04_test
input = day_04

input = input.split("\n")
floor = [list(r) for r in input]

accessible_spots = 0
for i, row in enumerate(floor):
    for j, spot in enumerate(row):
        if spot == "@":
            blank_spaces = 8
            # Check top left
            if i > 0 and j > 0:
                if floor[i - 1][j - 1] == "@":
                    blank_spaces -= 1
            # Check top
            if i > 0:
                if floor[i - 1][j] == "@":
                    blank_spaces -= 1
            # Check top right
            if i > 0 and j < len(row) - 1:
                if floor[i - 1][j + 1] == "@":
                    blank_spaces -= 1
            # Check left
            if j > 0:
                if row[j - 1] == "@":
                    blank_spaces -= 1
            # Check right
            if j < len(row) - 1:
                if row[j + 1] == "@":
                    blank_spaces -= 1
            # Check bottom left
            if i < len(floor) - 1 and j > 0:
                if floor[i + 1][j - 1] == "@":
                    blank_spaces -= 1
            # Check bottom
            if i < len(floor) - 1:
                if floor[i + 1][j] == "@":
                    blank_spaces -= 1
            # Check bottom right
            if i < len(floor) - 1 and j < len(row) - 1:
                if floor[i + 1][j + 1] == "@":
                    blank_spaces -= 1
            if blank_spaces >= 5:
                accessible_spots += 1

print(f"Part 1: {accessible_spots}")

def remove_rolls(floor):
    accessible_spots = 0
    removed_coords = []
    for i, row in enumerate(floor):
        for j, spot in enumerate(row):
            if spot == "@":
                blank_spaces = 8
                # Check top left
                if i > 0 and j > 0:
                    if floor[i - 1][j - 1] == "@":
                        blank_spaces -= 1
                # Check top
                if i > 0:
                    if floor[i - 1][j] == "@":
                        blank_spaces -= 1
                # Check top right
                if i > 0 and j < len(row) - 1:
                    if floor[i - 1][j + 1] == "@":
                        blank_spaces -= 1
                # Check left
                if j > 0:
                    if row[j - 1] == "@":
                        blank_spaces -= 1
                # Check right
                if j < len(row) - 1:
                    if row[j + 1] == "@":
                        blank_spaces -= 1
                # Check bottom left
                if i < len(floor) - 1 and j > 0:
                    if floor[i + 1][j - 1] == "@":
                        blank_spaces -= 1
                # Check bottom
                if i < len(floor) - 1:
                    if floor[i + 1][j] == "@":
                        blank_spaces -= 1
                # Check bottom right
                if i < len(floor) - 1 and j < len(row) - 1:
                    if floor[i + 1][j + 1] == "@":
                        blank_spaces -= 1
                if blank_spaces >= 5:
                    accessible_spots += 1
                    removed_coords.append([i, j])
    for coords in removed_coords:
        floor[coords[0]][coords[1]] = "."
    
    return accessible_spots, floor


removed = None
total_removed = 0
while removed != 0:
    removed, floor = remove_rolls(floor)
    total_removed += removed

print(f"Part 2: {total_removed}")