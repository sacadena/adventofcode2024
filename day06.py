DIRS = {
    '^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1),
}

NEXT_DIR = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}


def main():
    with open('data/day06_demo.txt') as h:
        matrix = h.readlines()

    start_row, start_col = find_start(matrix)
    symbol = matrix[start_row][start_col]
    seen = set()

    # Puzzle 1
    r, c = start_row, start_col
    dx, dy = DIRS[symbol]
    while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
        if matrix[r][c] == "#":
            r, c = r - dx, c - dy
            symbol = NEXT_DIR[symbol]
            dx, dy = DIRS[symbol]

        seen.add((r, c))
        r, c = r + dx, c + dy

    asw1 = len(seen)
    print(f"Puzzle 1: {asw1}")

    # Puzzle 2
    grid = {}
    for x, row in enumerate(matrix):
        for y, val in enumerate(row):
            grid[(x, y)] = val

    cnt_loops = 0
    for location in grid:
        step = set()
        current_loc = (start_row, start_col)
        symbol = '^'
        while True:
            x, y = current_loc
            dx, dy = DIRS[symbol]
            next_loc = (x + dx, y + dy)
            x_next, y_next = next_loc

            if not (0 <= x_next < len(matrix)) or not (0 <= y_next < len(matrix[0])):
                break

            if grid[(x_next, y_next)] == '#' or next_loc == location:
                symbol = NEXT_DIR[symbol]
                continue

            current_loc = next_loc

            if (next_loc, symbol) in step:
                cnt_loops += 1
                break

            step.add((next_loc, symbol))

    asw2 = cnt_loops
    print(f"Puzzle 2: {asw2}")


def find_start(matrix):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val in ('^', '>', 'v', '<'):
                return i, j


if __name__ == "__main__":
    main()
