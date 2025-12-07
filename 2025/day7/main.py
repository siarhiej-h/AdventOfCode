def part_one():
    grid = read_input()
    beam_start_column = grid[0].index('S')
    beams = {beam_start_column}
    splits = 0
    for i in range(1, len(grid)):
        new_beams = set()
        for beam in beams:
            if grid[i][beam] == '^':
                splits += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                new_beams.add(beam)
        beams = new_beams
    print(splits)


def part_two():
    grid = read_input()
    beam_start_column = grid[0].index('S')

    timelines_visited = dict()
    def dfs(i, beam):
        if (i, beam) in timelines_visited:
            return timelines_visited[(i, beam)]

        if i == len(grid) - 1:
            return 1

        if grid[i + 1][beam] == '^':
            result = dfs(i + 1, beam - 1) + dfs(i + 1, beam + 1)
        else:
            result = dfs(i + 1, beam)

        timelines_visited[(i, beam)] = result
        return result

    timelines = dfs(0, beam_start_column)
    print(timelines)


def read_input():
    grid = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            grid.append(line)

    return grid


if __name__ == '__main__':
    part_one()
    part_two()