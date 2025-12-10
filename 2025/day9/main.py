from itertools import combinations


def part_one():
    coordinates = read_input()
    max_area = 0
    for combination in combinations(coordinates, 2):
        point1, point2 = combination
        area = red_rectangle_area(point1, point2)
        max_area = max(area, max_area)
    print(max_area)


def red_rectangle_area(p1, p2):
    mix_x = min(p1[0], p2[0])
    max_x = max(p1[0], p2[0])
    mix_y = min(p1[1], p2[1])
    max_y = max(p1[1], p2[1])
    return abs((max_x - mix_x + 1) * (max_y - mix_y + 1))


def get_perimeter_coordinates(coordinates):
    coordinates = list(coordinates) + [coordinates[0]]
    perimeter_coordinates = set()
    for i in range(len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                perimeter_coordinates.add((x, y1))
        else:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                perimeter_coordinates.add((x1, y))
    return perimeter_coordinates


def part_two():
    coordinates = read_input()
    perimeter_coordinates = get_perimeter_coordinates(coordinates)

    max_area = 0
    for combination in combinations(coordinates, 2):
        point1, point2 = combination
        area = red_rectangle_area(point1, point2)
        if area <= max_area:
            continue

        if not is_perimeter_crossed(perimeter_coordinates, point1, point2):
            max_area = max(area, max_area)
    print(max_area)


def is_perimeter_crossed(perimeter_coordinates, point1, point2):
    mix_x = min(point1[0], point2[0])
    max_x = max(point1[0], point2[0])
    mix_y = min(point1[1], point2[1])
    max_y = max(point1[1], point2[1])
    for x, y in perimeter_coordinates:
        if mix_x < x < max_x and mix_y < y < max_y:
            return True
    return False


def read_input():
    grid = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip().split(',')
            grid.append(tuple(map(int, line)))

    return grid


if __name__ == '__main__':
    part_one()
    part_two()