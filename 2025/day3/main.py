def part_one():
    data = read_input()
    total = sum(find_joltage(bank, 2) for bank in data)
    print(total)


def part_two():
    data = read_input()
    total = sum(find_joltage(bank, 12) for bank in data)
    print(total)


def find_joltage(bank, jolts_to_find):
    start_index = 0
    jolts = []
    while jolts_to_find > 0:
        max_value = bank[start_index]
        max_index = start_index
        for i in range(start_index, len(bank) - jolts_to_find + 1):
            if bank[i] > max_value:
                max_index = i
                max_value = bank[i]
            if max_value == 9:
                break
        jolts.append(str(max_value))
        start_index = max_index + 1
        jolts_to_find -= 1

    joltage = int(''.join(jolts))
    return joltage


def read_input():
    data = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            all_jolts = [int(x) for x in line]
            data.append(all_jolts)
    return data


if __name__ == '__main__':
    part_one()
    part_two()