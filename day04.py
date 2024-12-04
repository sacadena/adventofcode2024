def main():
    with open('data/day04.txt') as h:
        contents = h.readlines()
    contents = [c.split('\n')[0] for c in contents]

    directions = [
        (-1, 0), (-1, -1), (0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (0, -1)
    ]

    count = 0

    for i, row in enumerate(contents):
        for j, val in enumerate(row):
            if val == 'X':
                for direction in directions:
                    if find_word(contents, 'XMAS', (i, j), direction):
                        count += 1

    print(f"Puzzle 1: {count}")

    count = 0

    for i, row in enumerate(contents):
        for j, val in enumerate(row):
            if val == 'A':
                if is_x_mas_around(contents, (i, j)):
                    count += 1

    print(f"Puzzle 2: {count}")


def is_x_mas_around(matrix, location):
    word = 'MAS'
    row, col = location
    possible_word_inds = (
        [(1, 1), (0, 0), (-1, -1)],
        [(-1, 1), (0, 0), (1, -1)],
    )
    words = [
        [
            matrix[row + dx][col + dy]
            for dx, dy in possible_word_ind
            if len(matrix) > (row + dx) >= 0 and len(matrix[0]) > (col + dy) >= 0
        ]
        for possible_word_ind in possible_word_inds
    ]
    return (
        (''.join(words[0]) == word or ''.join(reversed(words[0])) == word) and
        (''.join(words[1]) == word or ''.join(reversed(words[1])) == word)
    )


def find_word(matrix, word, location, direction) -> bool:
    dx, dy = direction
    row, col = location
    n = len(word)
    full_direction = [(dx * i, dy * i) for i in range(n)]
    word_in_matrix = [
        matrix[row + dxi][col + dyi]
        for dxi, dyi in full_direction
        if len(matrix) > (row + dxi) >= 0 and len(matrix[0]) > (col + dyi) >= 0
    ]
    return word == ''.join(word_in_matrix)


if __name__ == "__main__":
    main()
