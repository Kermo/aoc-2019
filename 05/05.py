with open('input.txt') as f:
    data = list(map(int, f.readline().split(",")))


def getIntCodeParam(modes, data, pointer, param):
    type = 0

    try:
        type = int(modes[-param])
    except:
        pass
    if (type == 0):
        return data[data[pointer + param]]
    else:
        return data[pointer + param]


def run_prgrm(data, user_input):
    pointer = 0

    while data[pointer] != 99:
        code = int(str(data[pointer])[-2:])
        modes = str(data[pointer])[:-2]

        if (code == 1):
            data[data[pointer + 3]] = getIntCodeParam(modes, data, pointer, 1)  + getIntCodeParam(modes, data, pointer, 2)
            pointer += 4
        elif (code == 2):
            data[data[pointer + 3]] = getIntCodeParam(modes, data, pointer, 1) * getIntCodeParam(modes, data, pointer, 2)
            pointer += 4
        elif (code == 3):
            data[data[pointer + 1]] = user_input
            pointer += 2
        elif (code == 4):
            print(getIntCodeParam(modes, data, pointer, 1))
            pointer += 2
        elif (code == 5):
            if (getIntCodeParam(modes, data, pointer, 1) != 0):
                pointer = getIntCodeParam(modes, data, pointer, 2)
            else:
                pointer += 3
        elif (code == 6):
            if (getIntCodeParam(modes, data, pointer, 1) == 0):
                pointer = getIntCodeParam(modes, data, pointer, 2)
            else:
                pointer += 3
        elif (code == 7):
            if (getIntCodeParam(modes, data, pointer, 1) < getIntCodeParam(modes, data, pointer, 2)):
                data[data[pointer + 3]] = 1
            else:
                data[data[pointer + 3]] = 0
            pointer += 4
        elif (code == 8):
            if (getIntCodeParam(modes, data, pointer, 1) == getIntCodeParam(modes, data, pointer, 2)):
                data[data[pointer + 3]] = 1
            else:
                data[data[pointer + 3]] = 0
            pointer += 4
        else:
            print(str(data[pointer]))
            break


# Part 1:
# run_prgrm(data, 1)

# Part 2:
run_prgrm(data, 5)
