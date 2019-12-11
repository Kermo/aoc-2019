import intcode

with open("input.txt") as f:
    data = list(map(lambda x: int(x), f.read().split(','))) + [0 for i in range(10000)]

intcode = intcode.IntCode(data)

def find_key_code():
    print("Part 1:")
    intcode.process(1, True)


def find_coordinates():
    print("Part 2:")
    intcode.process(2, True)

#find_key_code()
find_coordinates()