from collections import deque

NORTH = (-1, 0)
SOUTH = (1, 0)
WEST = (0, -1)
EAST = (0, 1)
NW = (-1, -1)
SW = (1, -1)
NE = (-1,  1)
SE = (1,  1)

CORNERS = [
    (NORTH, WEST,  NW),
    (SOUTH, WEST,  SW),
    (WEST, NORTH, NW),
    (EAST, NORTH, NE),
]


def main():
    with open('data/day12.txt') as h:
        contents = h.readlines()

    matrix = [list(c.strip('\n')) for c in contents]
    regions = get_regions(matrix)

    # Part one
    asw1 = 0
    for region in regions:
        area = len(region)
        perimeter = compute_perimeter(region)
        asw1 += area * perimeter

    print(f"Puzzle 1: {asw1}")

    # Part two
    asw2 = 0
    for region in regions:
        area = len(region)
        sides = count_sides(region)
        asw2 += area * sides

    print(f"Puzzle 2: {asw2}")


def get_regions(matrix):
    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]
    regions = []
    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                continue
            regions.append(bfs_region(i, j, matrix, visited))
    return regions


def bfs_region(i, j, matrix, visited):
    m, n = len(matrix), len(matrix[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    val = matrix[i][j]
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    region = []
    while queue:
        x, y = queue.popleft()
        region.append((x, y))

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and matrix[nx][ny] == val:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return region


def compute_perimeter(locations):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    loc_set = set(locations)

    perimeter = 0
    for (x, y) in locations:
        shared_edges = 4
        for dx, dy in dirs:
            if (x + dx, y + dy) in loc_set:
                shared_edges -= 1
        perimeter += shared_edges

    return perimeter


def count_sides(region):
    region_set = set(region)  # For fast membership
    edges = 0

    for (r, c) in region:
        for (check_offset, left_offset, diag_offset) in CORNERS:
            check_neighbor = (r + check_offset[0], c + check_offset[1])

            if check_neighbor not in region_set:
                left_neighbor = (r + left_offset[0], c + left_offset[1])
                diag_neighbor = (r + diag_offset[0], c + diag_offset[1])
                same_edge = (left_neighbor in region_set) and (diag_neighbor not in region_set)

                if not same_edge:
                    edges += 1

    return edges


if __name__ == "__main__":
    main()
