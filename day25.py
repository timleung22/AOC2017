class State(object):
    def __init__(self, registers, pos):
        self.switch = registers[pos]
        self.registers = registers
        self.pos = pos

    def run(self):
        pass

    def next(self):
        return None

class StateA(State):
    def run(self):
        if self.switch == 0:
            self.registers[self.pos] = 1
            self.pos += 1
        else:
            self.registers[self.pos] = 0
            self.pos -= 1

    def next(self):
        return StateB(self.registers, self.pos)

class StateB(State):
    def run(self):
        if self.switch == 0:
            self.registers[self.pos] = 0
            self.pos += 1
        else:
            self.registers[self.pos] = 1
            self.pos -= 1

    def next(self):
        if self.switch == 0:
            return StateC(self.registers, self.pos)
        else:
            return StateB(self.registers, self.pos)

class StateC(State):
    def run(self):
        if self.switch == 0:
            self.registers[self.pos] = 1
            self.pos += 1
        else:
            self.registers[self.pos] = 0
            self.pos -= 1

    def next(self):
        if self.switch == 0:
            return StateD(self.registers, self.pos)
        else:
            return StateA(self.registers, self.pos)

class StateD(State):
    def run(self):
        self.registers[self.pos] = 1
        self.pos -= 1

    def next(self):
        if self.switch == 0:
            return StateE(self.registers, self.pos)
        else:
            return StateF(self.registers, self.pos)

class StateE(State):
    def run(self):
        if self.switch == 0:
            self.registers[self.pos] = 1
        else:
            self.registers[self.pos] = 0
        self.pos -= 1

    def next(self):
        if self.switch == 0:
            return StateA(self.registers, self.pos)
        else:
            return StateD(self.registers, self.pos)

class StateF(State):
    def run(self):
        self.registers[self.pos] = 1
        if self.switch == 0:
            self.pos += 1
        else:
            self.pos -= 1

    def next(self):
        if self.switch == 0:
            return StateA(self.registers, self.pos)
        else:
            return StateE(self.registers, self.pos)


def Solution1():
    registers = [0 for i in range(12586542)]
    s = StateA(registers, int(len(registers)/2))
    for i in range(12586542):
        s.run()
        s = s.next()
    return sum(registers)

print(Solution1())

