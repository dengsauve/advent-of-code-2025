def rotate_clockwise(matrix):
    return [list(row) for row in zip(*matrix[::-1])]


def rotate_counter_clockwise(matrix):
    return [list(row) for row in zip(*matrix)][::-1]


def rotate_180(matrix):
    return [row[::-1] for row in matrix[::-1]]


def is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False

def multiline_str_to_matrix(input):
    matrix = [list(line) for line in input.strip().splitlines()]
    return matrix