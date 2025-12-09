from collections import defaultdict, deque


def part_one():
    grid = read_input()
    shortest_connections = dict()
    distances = compute_distances(grid)
    while len(shortest_connections) < 1000:
        min_distance, min_pair = get_closest_pair(distances, shortest_connections)
        shortest_connections[min_pair] = min_distance
    groups = find_groups(shortest_connections.keys())
    groups.sort(key=len, reverse=True)
    result = 1
    for group in groups[:3]:
        result *= len(group)
    print(result)


def compute_distances(grid):
    distances = []
    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            x1, y1, z1 = grid[i]
            x2, y2, z2 = grid[j]
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
            distances.append(((i, j), distance))
    distances.sort(key=lambda x: x[1])
    return distances


def get_closest_pair(precomputed, excluded_pairs):
    excluded = set(excluded_pairs)
    for (pos1, pos2), distance in precomputed:
        if (pos1, pos2) not in excluded and (pos2, pos1) not in excluded:
            return distance, (pos1, pos2)
    return None, None


def find_groups(edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = set()
    groups = []
    for node in adj:
        if node not in visited:
            group = []
            queue = deque([node])
            visited.add(node)
            while queue:
                current = queue.popleft()
                group.append(current)
                for neighbor in adj[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            groups.append(group)
    return groups


def part_two():
    grid = read_input()
    shortest_connections = dict()
    distances = compute_distances(grid)
    groups = []
    while not groups or len(groups[0]) != len(grid):
        min_distance, min_pair = get_closest_pair(distances, shortest_connections)
        shortest_connections[min_pair] = min_distance
        groups = find_groups(shortest_connections.keys())
    print(grid[min_pair[0]][0] * grid[min_pair[1]][0])


def read_input():
    grid = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip().split(',')
            grid.append(list(map(int, line)))

    return grid


if __name__ == '__main__':
    part_one()
    part_two()