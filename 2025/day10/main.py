import re
import itertools
import z3

def translate_diagram(diagram):
    return [1 if c == '#' else -1 for c in diagram]


def toggle(diagram, button):
    for pos in button:
        diagram[pos] *= -1


def find_sequence(buttons, clicks_total, start, desired_state, processor):
    for combination in itertools.combinations(buttons, clicks_total):
        current_state = start[:]
        for button in combination:
            processor(current_state, button)
            if current_state == desired_state:
                return combination
    return None


def part_one():
    data = read_input()
    total_clicks = 0
    for diagram, buttons, _ in data:
        translated_diagram = translate_diagram(diagram)
        start = [-1] * len(diagram)
        clicks_total = 0
        sequence = None
        while sequence is None:
            clicks_total += 1
            sequence = find_sequence(buttons, clicks_total, start, translated_diagram, toggle)
        total_clicks += clicks_total
    print(total_clicks)


def part_two():
    data = read_input()
    total_clicks = 0
    for _, buttons, target in data:
        minimum_clicks = find_minimum(buttons, target)
        total_clicks += minimum_clicks

    print(total_clicks)


def find_minimum(buttons, target):
    solver = z3.Solver()
    b_vars = [z3.Int(f"a{i}") for i in range(len(buttons))]
    for b in b_vars:
        solver.add(b >= 0)
    for i, target_joltage in enumerate(target):
        joltage_vars = []
        for j, button in enumerate(buttons):
            if i in button:
                joltage_vars.append(b_vars[j])
        solver.add(z3.Sum(joltage_vars) == target_joltage)

    minimum_clicks = None
    while solver.check() == z3.sat:
        model = solver.model()
        minimum_clicks = sum([model[x].as_long() for x in model])
        solver.add(z3.Sum(b_vars) < minimum_clicks)
    return minimum_clicks


def read_input():
    data = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            diagram = re.search(r'\[([.#]+)]', line).group(1)
            buttons = [list(map(int, t.split(','))) for t in re.findall(r'\(([\d,]+)\)', line)]
            joltage_requirements = list(map(int, re.search(r'\{([\d,]+)}', line).group(1).split(',')))
            data.append((diagram, buttons, joltage_requirements))

    return data


if __name__ == '__main__':
    part_one()
    part_two()