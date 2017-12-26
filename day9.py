class Context(object):
    def __init__(self):
        self.level = 0
        self.score = 0
        self.inGarbage = False
        self.skipping = False
        self.garbage = 0

    def ignoring(self):
        return self.inGarbage or self.skipping

def curlyBegins(ctx):
    if not ctx.ignoring():
        ctx.level += 1
        ctx.score += ctx.level
    else:
        if ctx.skipping:
            ctx.skipping = False
        else:
            ctx.garbage += 1

def bang(ctx):
    # ignore this ! if I am skipping, and turn off skipping
    ctx.skipping = not ctx.skipping

def curlyEnds(ctx):
    if not ctx.ignoring():
        ctx.level -= 1
    else:
        if ctx.skipping:
            ctx.skipping = False
        else:
            ctx.garbage += 1

def angleBegins(ctx):
    if not ctx.ignoring():
        ctx.inGarbage = True
    else:
        if ctx.skipping:
            ctx.skipping = False
        else:
            ctx.garbage += 1

def angleEnds(ctx):
    if not ctx.skipping:
        if ctx.inGarbage:
            ctx.inGarbage = False
    else:
        ctx.skipping = False

def process(file):
    operations = {
        '{' : curlyBegins,
        '}' : curlyEnds,
        '!' : bang,
        '<' : angleBegins,
        '>' : angleEnds,
    }
    context = Context()
    nRead = 0
    with open(file, "r") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            else:
                nRead += 1
                if context.level < 0:
                    print("Something went wrong")
                processCharacter(c, operations, context)
    return context.garbage

def processCharacter(c, operations, context):
    if c in operations.keys():
        operations[c](context)
    elif context.skipping:
        context.skipping = False
    elif context.inGarbage:
        context.garbage += 1

def testMe(characters):
    operations = {
        '{' : curlyBegins,
        '}' : curlyEnds,
        '!' : bang,
        '<' : angleBegins,
        '>' : angleEnds,
    }
    context = Context()
    for eachCharacater in characters:
        processCharacter(eachCharacater, operations, context)
    return context.score

print(testMe("{{<{}!>,>{}}}"))

print(process("day9Input.txt"))

