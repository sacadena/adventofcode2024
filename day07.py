def main():
    with open('data/day07.txt') as h:
        instructions = h.readlines()

    instructions = list(map(parse_instruction, instructions))

    asw1 = sum(
        expected for expected, nums in instructions
        if is_instruction_valid_part_1((expected, nums))
    )
    print(f"Puzzle 1: {asw1}")

    asw2 = sum(
        expected for expected, nums in instructions
        if is_instruction_valid_part_2((expected, nums))
    )
    print(f"Puzzle 2: {asw2}")


def is_instruction_valid_part_1(instr):
    expected, nums = instr

    def dfs(ind, current):
        if ind == len(nums) - 1:
            return current == expected
        plus = dfs(ind + 1, current=current + nums[ind + 1])
        if plus:
            return True
        return dfs(ind + 1, current=current * nums[ind + 1])

    return dfs(ind=0, current=nums[0])


def is_instruction_valid_part_2(instr):
    expected, nums = instr

    def dfs(ind, current):
        if ind == len(nums) - 1:
            return current == expected
        plus = dfs(ind + 1, current=current + nums[ind + 1])
        if plus:
            return True

        mult = dfs(ind + 1, current=current * nums[ind + 1])
        if mult:
            return mult

        return dfs(ind + 1, current=int(str(current) + str(nums[ind + 1])))

    return dfs(ind=0, current=nums[0])


def parse_instruction(instruction):
    expected, numbers = instruction.split(':')
    return int(expected), list(map(int, numbers.split()))


if __name__ == '__main__':
    main()