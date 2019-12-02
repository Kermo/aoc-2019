with open("input.txt") as f:
    data = f.read()
    split_data = [int(x) for x in data.split(",")]


def part1(data, noun=12, verb=2):
    index = 0
    program = data[:]
    program[1] = noun
    program[2] = verb
    while True:
        if program[index] == 1:
            program[program[index + 3]] = program[program[index + 1]] + program[program[index + 2]]
        elif program[index] == 2:
            program[program[index + 3]] = program[program[index + 1]] * program[program[index + 2]]
        elif program[index] == 99:
            break
        else:
            break
        index += 4

    return program[0]


def part2(data):
    for noun in range(100):
        for verb in range(100):
            if part1(data, noun, verb) == 19690720:
                return 100 * noun + verb

print("Part 1: " + str(part1(split_data)))
print("Part 2: " + str(part2(split_data)))