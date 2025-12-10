from input import day_08_test, day_08
import math
from collections import namedtuple

JunctionBox = namedtuple('JunctionBox', ['x', 'y', 'z'])

def get_3d_distance(a, b):
    return math.sqrt(
        (a.x - b.x)**2 +
        (a.y - b.y)**2 +
        (a.z - b.z)**2
    )


def part1(input, number_of_connections):
    junction_boxes = []
    distances = []
    connections = [] # [[a, b, d], [c, e, f], ...]

    for line in input:
        x, y, z = map(int, line.split(","))
        junction_boxes.append(JunctionBox(x, y, z))
    
    for i in junction_boxes:
        for j in junction_boxes:
            if i != j:
                distance = get_3d_distance(i, j)
                distances.append([distance, i, j])
    
    distances.sort()

    for i in range(number_of_connections):
        distance = distances.pop(0)
        a, b = distance[1:]
        connected = False
        for connection in connections:
            if connected:
                break
            if a in connection:
                if b not in connection:
                    connection.append(b)
                    connected = True
            elif b in connection:
                if a not in connection:
                    connection.append(a)
                    connected = True
        if not connected:
            connections.append([a, b])
    
    connections.sort(key=len, reverse=True)

    product = len(connections[0])
    for i in range(1,3):
        product *= len(connections[i])
    
    return product


    

def part2(input):
    pass


def main():
    test_input = day_08_test.split("\n")
    challenge_input = day_08.split("\n")
    
    print("=== Test Input ===")

    total = part1(test_input, 10)
    print(f"Part 1: {total}")
    assert total == 40

    total = part2(test_input)
    print(f"Part 2: {total}")
    # assert total == 40

    print(f"\n=== Challenge Input: ===")

    total = part1(challenge_input, 1000)
    print(f"Part 1: {total}")

    total = part2(challenge_input)
    print(f"Part 2: {total}")


if __name__ == "__main__":
    main()