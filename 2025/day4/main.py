def part_one():
    data = read_input()
    accessible = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            cell = data[row][col]
            if cell == "@" and calculate_adjucent_cells(data, row, col) < 4:
                accessible += 1
    print(accessible)


def calculate_adjucent_cells(data, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    total = 0
    for direction in directions:
        r_diff, c_diff = direction
        new_row = row + r_diff
        new_col = col + c_diff
        if 0 <= new_row < len(data) and 0 <= new_col < len(data[row]):
            cell = data[new_row][new_col]
            if cell == "@":
                total += 1
    return total


def part_two():
    grid = read_input()
    total_removed = 0
    moved_this_round = True
    while moved_this_round:
        moved_this_round = False
        new_grid = []
        for row in range(len(grid)):
            new_row = ""
            for col in range(len(grid[row])):
                cell = grid[row][col]
                if cell == "@" and calculate_adjucent_cells(grid, row, col) < 4:
                    new_row += "."
                    total_removed += 1
                    moved_this_round = True
                else:
                    new_row += cell
            new_grid.append(new_row)
        grid = new_grid
    print(total_removed)


def read_input():
    data = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)
    return data


if __name__ == '__main__':
    part_one()
    part_two()