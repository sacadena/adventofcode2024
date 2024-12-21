def main():
    with open('data/day09.txt') as h:
        content = h.read().strip()

    # part one
    disk = parse_input(content)
    compact_disk(disk)
    asw1 = checksum(disk)
    print(f"Puzzle 1: {asw1}")

    # part two
    blocks = uncompress_code_to_blocks(content)
    compact_part2_blocks(blocks)
    asw2 = checksum_block(blocks)
    print(f"Puzzle 2: {asw2}")


def parse_input(code):
    disk = []
    file_id = 0
    digits = [int(c) for c in code if c.isdigit()]

    for i in range(0, len(digits), 2):
        file_size = digits[i]
        free_size = digits[i + 1] if i + 1 < len(digits) else 0
        if file_size > 0:
            disk.append((file_id, file_size))
            file_id += 1
        if free_size > 0:
            disk.append((None, free_size))

    return disk


def compact_disk(disk):
    def pop_file():
        for i in range(len(disk) - 1, -1, -1):
            fid, size = disk[i]
            if fid is not None:
                disk.pop(i)
                return (fid, size)
        return None

    def leftmost_free():
        for idx, (fid, _) in enumerate(disk):
            if fid is None:
                return idx
        return -1

    def done():
        found_free = False
        for fid, _ in disk:
            if fid is None:
                found_free = True
            elif fid is not None and found_free:
                return False
        return True

    current_file = pop_file()
    while current_file and not done():
        (fid, fsize) = current_file
        free_index = leftmost_free()
        if free_index == -1:
            break

        free_size = disk[free_index][1]

        if fsize > free_size:
            disk[free_index] = (fid, free_size)
            leftover = fsize - free_size
            current_file = (fid, leftover)
        elif fsize < free_size:
            disk[free_index] = (fid, fsize)
            leftover_free = free_size - fsize
            disk.insert(free_index + 1, (None, leftover_free))
            current_file = pop_file()
        else:
            disk[free_index] = (fid, fsize)
            current_file = pop_file()

    if current_file:
        idx = leftmost_free()
        if idx >= 0:
            disk[idx] = current_file


def uncompress_code_to_blocks(code):
    blocks = []
    digits = [int(ch) for ch in code if ch.isdigit()]

    file_id = 0
    i = 0
    while i < len(digits):
        file_size = digits[i]
        free_size = digits[i + 1] if i + 1 < len(digits) else 0
        i += 2

        if file_size > 0:
            blocks.extend([str(file_id)] * file_size)
            file_id += 1

        if free_size > 0:
            blocks.extend(['.'] * free_size)

    return blocks


def compact_part2_blocks(blocks):
    all_ids = set(block for block in blocks if block != '.')
    sorted_ids = sorted(all_ids, key=lambda x: int(x), reverse=True)

    for fid_str in sorted_ids:
        positions = [i for i, b in enumerate(blocks) if b == fid_str]
        if not positions:
            continue

        file_size = len(positions)
        first_block_idx = positions[0]

        target_span_start = find_free_span(blocks, 0, first_block_idx, file_size)
        if target_span_start is None:
            continue

        for offset in range(file_size):
            blocks[target_span_start + offset] = fid_str

        for pos in positions:
            blocks[pos] = '.'


def find_free_span(disk_blocks, start_idx, end_idx, needed):
    consecutive = 0
    span_start = -1

    for i in range(start_idx, end_idx):
        if disk_blocks[i] == '.':
            consecutive += 1
            if consecutive == 1:
                span_start = i

            if consecutive == needed:
                return span_start
        else:
            consecutive = 0
            span_start = -1

    return None


def checksum(disk):
    chksum = 0
    block_pos = 0
    for fid, size in disk:
        if fid is not None:
            for offset in range(size):
                chksum += fid * (block_pos + offset)
        block_pos += size
    return chksum


def checksum_block(disk_blocks):
    total = 0
    for pos, val in enumerate(disk_blocks):
        if val != '.':
            fid = int(val)
            total += fid * pos
    return total


if __name__ == "__main__":
    main()
