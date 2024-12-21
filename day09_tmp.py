def main():
    # Change 'data/day09_demo.txt' to your actual puzzle input file, e.g. 'data/day09.txt'
    with open('data/day09.txt', 'r') as f:
        puzzle_input = f.read().strip()

    # 1) Expand into an array of blocks, each block is either '.' or '<file_id>'
    disk_blocks = uncompress_code_to_blocks(puzzle_input)

    # 2) Compact with Part Two rules (whole-file moves, once, highest ID first)
    compact_part2_blocks(disk_blocks)

    # 3) Compute and print final checksum
    chksum = checksum(disk_blocks)
    print(f"Part 2 checksum: {chksum}")


def uncompress_code_to_blocks(code):
    """
    Given a puzzle input like '2333133121414131402', expand it into
    an array of individual blocks, e.g.:
      disk_blocks = ['0','0','.', '.', '.', '1','1','1', '.', '.', '.', '2', ... ]
    Each file gets a unique string ID: '0', '1', '2', ..., etc.

    The digits in 'code' alternate: (file_size, free_size, file_size, free_size, ...)
    We'll keep a running file_id counter (as an integer), but store it as a string in the blocks.
    """
    blocks = []
    digits = [int(ch) for ch in code if ch.isdigit()]

    file_id = 0
    i = 0
    while i < len(digits):
        file_size = digits[i]
        free_size = digits[i + 1] if i + 1 < len(digits) else 0
        i += 2

        # Add 'file_size' blocks of file_id
        if file_size > 0:
            blocks.extend([str(file_id)] * file_size)
            file_id += 1

        # Add 'free_size' blocks of '.'
        if free_size > 0:
            blocks.extend(['.'] * free_size)

    return blocks


def compact_part2_blocks(blocks):
    all_ids = set(block for block in blocks if block != '.')
    sorted_ids = sorted(all_ids, key=lambda x: int(x), reverse=True)

    for fid_str in sorted_ids:
        # Find all the positions of this file
        positions = [i for i, b in enumerate(blocks) if b == fid_str]
        if not positions:
            continue  # no blocks of this file found?

        file_size = len(positions)
        first_block_idx = positions[0]

        # Attempt to find a free span from index 0 up to first_block_idx-1
        # that is large enough to hold file_size blocks
        target_span_start = find_free_span(blocks, 0, first_block_idx, file_size)
        if target_span_start is None:
            # Not enough space to the left, skip moving
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


def checksum(disk_blocks):
    """
    Compute the puzzle's checksum on the final arrangement:
      sum of (int(file_id) * block_position) for each file block.
    Free blocks ('.') are skipped.
    """
    total = 0
    for pos, val in enumerate(disk_blocks):
        if val != '.':
            fid = int(val)
            total += fid * pos
    return total


if __name__ == "__main__":
    main()
