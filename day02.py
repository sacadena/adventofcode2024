from copy import copy


def main():
    with open('data/day02.txt') as h:
        contents = h.readlines()
    contents = [c.split('\n')[0] for c in contents]

    count_safe = 0
    for line in contents:
        levels = list(map(int, line.split()))
        if is_safe(levels):
            count_safe += 1

    print(f"Puzzle 1: {count_safe}")

    count_safe = 0
    for line in contents:
        levels = list(map(int, line.split()))
        if is_safe(levels):
            count_safe += 1
        else:
            for i in range(len(levels)):
                levels_removed = copy(levels)
                levels_removed.pop(i)
                if is_safe(levels_removed):
                    count_safe += 1
                    break

    print(f"Puzzle 2: {count_safe}")


def is_safe(levels) -> bool:
    differences = [l1 - l2 for l1, l2 in zip(levels, levels[1:])]
    return (
            (
                    all([d > 0 for d in differences]) or
                    all([d < 0 for d in differences])
            ) and
            all([1 <= abs(d) <= 3 for d in differences])
    )


if __name__ == '__main__':
    main()