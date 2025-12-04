def part_one():
    data = read_input()
    position = 50
    total = 0
    for direction, distance in data:
        if direction == 'L':
            position -= distance
        elif direction == 'R':
            position += distance

        position %= 100
        if position == 0:
            total += 1

    print(total)


def part_two():
    data = read_input()
    position = 50
    total = 0
    for direction, distance in data:
        for _ in range(distance):
            if direction == 'L':
                position -= 1
            else:
                position += 1

            if position < 0:
                position = 99
            elif position == 100:
                position = 0

            if position == 0:
                total += 1

    print(total)


def read_input():
    data = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])
            data.append((direction, distance))
    return data


if __name__ == '__main__':
    part_one()
    part_two()