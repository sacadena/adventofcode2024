from collections import defaultdict


def main():
    with open('data/day08.txt') as h:
        matrix = h.readlines()

    matrix = [row.rstrip('\n') for row in matrix]
    m = len(matrix)
    n = len(matrix[0])

    position_antennas = defaultdict(list)

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val != '.':
                position_antennas[val].append((i, j))

    # Part 1
    total_anti_nodes = []
    for key, positions in position_antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                total_anti_nodes.extend(
                    get_anti_nodes_from_pair_part1(positions[i], positions[j], m, n)
                )

    asw1 = len(set(total_anti_nodes))
    print(f"Puzzle 1: {asw1}")

    # Part 2
    total_anti_nodes = []
    for key, positions in position_antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                total_anti_nodes.extend(
                    get_anti_nodes_from_pair_part2(positions[i], positions[j], m, n)
                )

    asw2 = len(set(total_anti_nodes))
    print(f"Puzzle 2: {asw2}")


def get_anti_nodes_from_pair_part1(pos1, pos2, n_rows, n_cols):
    r1, c1 = pos1
    r2, c2 = pos2
    dr = r1 - r2
    dc = c1 - c2

    locations = []
    if 0 <= (r1 + dr) < n_rows and 0 <= (c1 + dc) < n_cols:
        locations.append((r1 + dr, c1 + dc))
    if 0 <= (r2 - dr) < n_rows and 0 <= (c2 - dc) < n_cols:
        locations.append((r2 - dr, c2 - dc))
    return locations


def get_anti_nodes_from_pair_part2(pos1, pos2, n_rows, n_cols):
    r1, c1 = pos1
    r2, c2 = pos2
    dr = r1 - r2
    dc = c1 - c2

    locations = []
    nothing_added = False
    multiplier = 0
    while not nothing_added:
        l1, l2 = None, None
        if 0 <= (r1 + dr * multiplier) < n_rows and 0 <= (c1 + dc * multiplier) < n_cols:
            l1 = (r1 + dr * multiplier, c1 + dc * multiplier)
        if 0 <= (r2 - dr * multiplier) < n_rows and 0 <= (c2 - dc * multiplier) < n_cols:
            l2 = (r2 - dr * multiplier, c2 - dc * multiplier)

        if l1 is not None:
            locations.append(l1)
        if l2 is not None:
            locations.append(l2)

        multiplier += 1

        if l1 is None and l2 is None:
            nothing_added = True

    return locations


if __name__ == "__main__":
    main()


