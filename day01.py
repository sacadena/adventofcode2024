from collections import defaultdict


def main():
    with open('data/day01.txt') as h:
        contents = h.readlines()
    contents = [c.split('\n')[0] for c in contents]
    list_1, list_2 = zip(*[map(int, c.split()) for c in contents])
    asw1 = puzzle1(list_1, list_2)
    print(f"Puzzle 1: {asw1}")
    asw2 = puzzle2(list_1, list_2)
    print(f"Puzzle 2: {asw2}")


def puzzle1(list_1, list_2):
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)
    return sum([abs(l1 - l2) for l1, l2 in zip(sorted_list_1, sorted_list_2)])


def puzzle2(list1, list2):
    counts = defaultdict(int)
    for c in list2:
        counts[c] += 1

    result = 0
    for l1 in list1:
        result += l1 * counts[l1]

    return result


if __name__ == '__main__':
    main()
