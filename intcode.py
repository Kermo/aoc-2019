class IntCode:
    def __init__(self, data):
        self.memory = data
        self.pointer = 0
        self.size = len(data)
        self.out = 0
        self.halt = False
        self.initialized = False
        self.relBase = 0

    def process(self, inputArg=None, VERBOSE=True):
        if inputArg != None:
            self.initialized = True

        while self.pointer < self.size:

            opcode = int(str(self.memory[self.pointer])[-2:])
            paramModes = str(self.memory[self.pointer])[:-2]

            if (opcode == 99):
                self.halt = True
                break
            elif (opcode == 1):
                self.setParam(paramModes, 3, self.getParam(paramModes, 1) + self.getParam(paramModes, 2))
                self.pointer += 4
            elif (opcode == 2):
                self.setParam(paramModes, 3, self.getParam(paramModes, 1) * self.getParam(paramModes, 2))
                self.pointer += 4
            elif (opcode == 3):
                if inputArg != None:
                    self.setParam(paramModes, 1, inputArg)
                    inputArg = None
                else:
                    if VERBOSE:
                        self.setParam(paramModes, 1, int(input("Type int > ")))
                    else:
                        break
                self.pointer += 2
            elif (opcode == 4):
                out = self.getParam(paramModes, 1)
                if VERBOSE:
                    print(">> " + str(out))
                self.out = out
                self.pointer += 2
            elif (opcode == 5):
                if (self.getParam(paramModes, 1) != 0):
                    self.pointer = self.getParam(paramModes, 2)
                else:
                    self.pointer += 3
            elif (opcode == 6):
                if (self.getParam(paramModes, 1) == 0):
                    self.pointer = self.getParam(paramModes, 2)
                else:
                    self.pointer += 3
            elif (opcode == 7):
                if (self.getParam(paramModes, 1) < self.getParam(paramModes, 2)):
                    self.setParam(paramModes, 3, 1)
                else:
                    self.setParam(paramModes, 3, 0)
                self.pointer += 4
            elif (opcode == 8):
                if (self.getParam(paramModes, 1) == self.getParam(paramModes, 2)):
                    self.setParam(paramModes, 3, 1)
                else:
                    self.setParam(paramModes, 3, 0)
                self.pointer += 4
            elif opcode == 9:
                self.relBase += self.getParam(paramModes, 1)
                self.pointer += 2
            else:
                print(str(self.memory[self.pointer]) + " Something went wrong :(")
                break

    def getParam(self, paramModes, param):
        return self.memory[self.getParamAddress(paramModes, param)]

    def setParam(self, paramModes, param, value):
        self.memory[self.getParamAddress(paramModes, param)] = value

    def getParamAddress(self, paramModes, param):
        type = 0
        try:
            type = int(paramModes[-param])
        except:
            pass
        if type == 0:
            return self.memory[self.pointer + param]
        elif type == 1:
            return self.pointer + param
        elif type == 2:
            offset = self.memory[self.pointer + param]
            return self.relBase + offset
        else:
            print('Param type error')
            return 0