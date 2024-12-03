def main():
    with open('data/day03.txt') as h:
        contents = h.read()

    asw1 = multiply_valid_pairs_and_sum(contents)
    print(f"Puzzle 1: {asw1}")

    asw2 = 0
    dos = contents.split('do()')
    for do in dos:
        asw2 += multiply_valid_pairs_and_sum(do.split("don't()")[0])

    print(f"Puzzle 2: {asw2}")


def multiply_valid_pairs_and_sum(line):
    num_pairs = []
    for sec in line.split('mul(')[1:]:
        sec_split = sec.split(')')
        if len(sec_split) > 0:
            potential_nums = sec_split[0].split(',')
            if len(potential_nums) == 2:
                a, b = potential_nums
                if a.isnumeric() and b.isnumeric():
                    num_pairs.append((int(a), int(b)))
    return sum(a * b for (a, b) in num_pairs)


if __name__ == "__main__":
    main()
