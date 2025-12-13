def build_connections(data):
    connections = dict()
    for device, outputs in data:
        connections[device] = outputs
    return connections


def part_one():
    data = read_input()
    connections = build_connections(data)

    start = "you"
    target = "out"
    devices_to_check = [start]
    total = 0
    while devices_to_check:
        current = devices_to_check.pop()
        if current == target:
            total += 1
            continue
        for output in connections[current]:
            devices_to_check.append(output)
    print(total)


def part_two():
    data = read_input()
    connections = build_connections(data)

    start = "svr"
    target = "out"
    devices_checked = dict()
    def dfs(current, dac_found, fft_found):
        if (current, dac_found, fft_found) in devices_checked:
            return devices_checked[(current, dac_found, fft_found)]

        if current == "dac":
            dac_found = True
        if current == "fft":
            fft_found = True

        if current == target:
            if dac_found and fft_found:
                return 1
            return 0

        count = 0
        for output in connections[current]:
            count += dfs(output, dac_found, fft_found)

        devices_checked[(current, dac_found, fft_found)] = count
        return count

    total = dfs(start, False, False)
    print(total)


def read_input():
    data = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            parts = line.split(": ")
            device = parts[0]
            outputs = parts[1].split()
            data.append((device, outputs))

    return data


if __name__ == '__main__':
    part_one()
    part_two()