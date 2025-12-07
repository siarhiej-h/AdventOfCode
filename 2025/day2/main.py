def part_one():
    data = read_input()
    all_invalid_ids = []
    for r0, r1 in data:
        for id_value in range(r0, r1 + 1):
            id_str = str(id_value)
            if is_invalid(id_str, repetitions=2):
                all_invalid_ids.append(id_value)
    print(sum(all_invalid_ids))


# def is_invalid(id_value):
#     if len(id_value) % 2 != 0:
#         return False
#     return id_value[0: len(id_value)//2] == id_value[len(id_value)//2:]


def is_invalid(id_value, repetitions=None):
    n = len(id_value)
    if repetitions is not None and n % repetitions != 0:
        return False

    if repetitions is not None:
        sub_lengths = [n // repetitions]
    else:
        sub_lengths = list(range(1, n // 2 + 1))

    for sub_len in sub_lengths:
        if n % sub_len == 0:
            sub = id_value[:sub_len]
            if sub * (n // sub_len) == id_value:
                return True
    return False


def part_two():
    data = read_input()
    all_invalid_ids = []
    for r0, r1 in data:
        for id_value in range(r0, r1 + 1):
            id_str = str(id_value)
            if is_invalid(id_str):
                all_invalid_ids.append(id_value)
    print(sum(all_invalid_ids))


def read_input():
    data = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            all_ranges = line.split(",")
            for r in all_ranges:
                bounds = r.split("-")
                data.append((int(bounds[0]), int(bounds[1])))
    return data


if __name__ == '__main__':
    part_one()
    part_two()