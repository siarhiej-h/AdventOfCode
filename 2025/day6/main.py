def part_one():
    data = read_input()
    data = [line.split() for line in data]
    total = 0
    for col in range(len(data[0])):
        operation = data[-1][col]
        answer = int(data[0][col])
        for row in range(1, len(data) - 1):
            value = int(data[row][col])
            if operation == '+':
                answer += value
            elif operation == '*':
                answer *= value
        total += answer
    print(total)


def part_two():
    data = read_input()
    operators = data[-1].split()

    operations = 0
    start_index = 0
    total = 0
    while operations < len(operators):
        if operations == len(operators) - 1:
            end_index = len(data[0]) - 2
        else:
            end_index = data[-1].index(operators[operations + 1], start_index + 1) - 2
        operands = []
        operator = operators[operations]
        for col in range(start_index, end_index + 1):
            digits = ""
            for row in range(0, len(data) - 1):
                value = data[row][col]
                if value.isdigit():
                    digits += value

            operands.append(int(digits))
        answer = operands[0]
        for operand in operands[1:]:
            if operator == '+':
                answer += operand
            elif operator == '*':
                answer *= operand
        total += answer
        operations += 1
        start_index = end_index + 2
    print(total)


def read_input():
    data = []
    with open('input.txt') as f:
        for line in f.readlines():
            data.append(line)
    return data


if __name__ == '__main__':
    part_one()
    part_two()