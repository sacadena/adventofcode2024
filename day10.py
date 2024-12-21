def main():
    with open('data/day10.txt') as h:
        content = h.readlines()

    content = [c.rstrip('\n') for c in content]
    matrix = [list(map(int, row)) for row in content]

    heads = []
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 0:
                heads.append((i, j))

    # Part one
    asw1 = 0
    for head in heads:
        asw1 += compute_score_head(head, matrix)
    print(f"Puzzle 1: {asw1}")

    # Part two
    asw2 = 0
    for head in heads:
        asw2 += compute_rating_head(head, matrix)
    print(f"Puzzle 2: {asw2}")


def compute_score_head(head, matrix):
    r, c = head
    m = len(matrix)
    n = len(matrix[0])
    tail = 9

    outputs = []

    def dfs(node, target):
        i, j = node
        val = matrix[i][j]

        if val != target:
            return

        if val == tail:
            outputs.append(node)

        neighs = get_neighbours(node, m, n)

        for neigh in neighs:
            dfs(neigh, target + 1)

    dfs((r, c), 0)
    return len(set(outputs))


def compute_rating_head(head, matrix):
    r, c = head
    m = len(matrix)
    n = len(matrix[0])
    tail = 9

    outputs = []

    def dfs(node, target):
        i, j = node
        val = matrix[i][j]

        if val != target:
            return 0

        if val == tail:
            return 1

        neighs = get_neighbours(node, m, n)

        return sum(dfs(neigh, target + 1) for neigh in neighs)

    return dfs((r, c), 0)


def get_neighbours(node, m, n):
    i, j = node
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighs = []
    for delta in deltas:
        dx, dy = delta
        if 0 <= (i + dx) < m and 0 <= (j + dy) < n:
            neighs.append((i + dx, j + dy))
    return neighs


if __name__ == "__main__":
    main()
