def part_one():
    shapes, regions = read_input()
    count = 0
    for region_size, presents_required in regions:
        w, h = region_size
        total_presents = sum(presents_required) * 9
        area = w * h
        if area >= total_presents:
            count += 1
    print(count)


def read_input():
    shapes = []
    regions = []
    is_shape = False
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            if is_shape is False and line.endswith(":"):
                is_shape = True
                shape = []
                continue

            if line == "":
                if is_shape:
                    shapes.append(shape)
                is_shape = False
                continue

            if is_shape:
                shape.append(line)
                continue

            if not is_shape:
                parts = line.split(":")
                region_size = list(map(int, parts[0].split("x")))
                presents_required = list(map(int, parts[1].split()))
                regions.append((region_size, presents_required))

    return shapes, regions


if __name__ == '__main__':
    part_one()