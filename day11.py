def main():
    with open('data/day11.txt') as h:
        content = h.read()

    init_stones = list(map(int, content.split()))

    # Part one
    n_blinks = 25
    stones = init_stones
    for i in range(n_blinks):
        stones = blink(stones)

    asw1 = len(stones)
    print(f"Puzzle 1: {asw1}")

    # Part two

    n_blinks = 75
    table = {}

    def dfs(st, ind):
        if ind == n_blinks:
            return 1

        if (st, ind) in table:
            return table[(st, ind)]

        new_stones = apply_rules(st)

        tot = 0
        for ns in new_stones:
            tot += dfs(ns, ind + 1)

        table[(st, ind)] = tot
        return tot

    asw2 = 0
    for stone in init_stones:
        asw2 += dfs(stone, 0)

    print(f"Puzzle 2: {asw2}")


def blink(stones):
    new_stones = []
    for stone in stones:
        new_stones_here = apply_rules(stone)
        new_stones.extend(new_stones_here)
    return new_stones


def apply_rules(stone):
    if stone == 0:
        return [1]
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        n = len(str_stone)
        left = int(''.join(list(str_stone)[:n//2]))
        right = int(''.join(list(str_stone)[n//2:]))
        return [left, right]
    return [stone * 2024]


if __name__ == "__main__":
    main()
