import intcode

with open('input.txt') as f:
    data = list(map(int, f.readline().split(",")))

# Part 1:
intcode = intcode.IntCode(data)
#intcode.process(1, True)

# Part 2:
intcode.process(5, True)
