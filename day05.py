from copy import copy


def main():
    with open('data/day05.txt') as h:
        contents = h.read()

    rules, protocols = contents.split("\n\n")

    rules = rules.split("\n")
    rules = [tuple(map(int, (r.split('|')))) for r in rules]

    protocols = protocols.split("\n")
    protocols = [list(map(int, p.split(','))) for p in protocols]

    # Puzzle 1
    asw1 = 0
    for protocol in protocols:
        if is_valid_protocol(protocol, rules):
            asw1 += protocol[len(protocol) // 2]

    print(f"Puzzle 1: {asw1}")

    # Puzzle 2
    asw2 = 0
    for protocol in protocols:
        if not is_valid_protocol(protocol, rules):
            ordered = copy(protocol)

            # Order it
            while not is_valid_protocol(ordered, rules):
                for (before, after) in rules:
                    if before in ordered and after in ordered:
                        bi = ordered.index(before)
                        ai = ordered.index(after)
                        if bi > ai:
                            ordered.remove(before)
                            ordered.insert(ai, before)

            asw2 += ordered[len(ordered) // 2]

    print(f"Puzzle 2: {asw2}")


def is_valid_protocol(protocol, rules) -> bool:
    for (before, after) in rules:
        if before in protocol and after in protocol:
            if protocol.index(before) > protocol.index(after):
                return False
    return True


if __name__ == "__main__":
    main()
