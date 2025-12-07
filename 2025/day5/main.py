def part_one():
    ranges, ingredients = read_input()

    total = 0
    for ingredient in ingredients:
        is_fresh = False
        for r in ranges:
            start, end = r
            if start <= ingredient <= end:
                is_fresh = True
                break
        if is_fresh:
            total += 1
    print(total)


def merge_ranges(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    for start, end in ranges:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


def part_two():
    ranges, _ = read_input()
    ranges = merge_ranges(ranges)
    total_fresh = 0
    for r in ranges:
        start, end = r
        total_fresh += end - start + 1

    print(total_fresh)


def read_input():
    ranges = []
    ingredients = []
    is_ranges = True
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                is_ranges = False
                continue

            if is_ranges:
                start, end = line.split("-")
                ranges.append((int(start), int(end)))
            else:
                ingredients.append(int(line))

    return ranges, ingredients


if __name__ == '__main__':
    part_one()
    part_two()