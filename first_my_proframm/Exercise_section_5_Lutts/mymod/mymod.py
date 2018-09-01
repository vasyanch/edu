def countLines(name):
    name.seek(0)
    return len(name.readlines())
    
def countChars(name):
    name.seek(0)
    return len(name.read())

def test(name):
    name = open(name)
    return countLines(name), countChars(name)

# For big file if not enough memory

def countLines_big(name):
    name.seek(0)
    tot = 0
    for line in name: tot +=1
    return tot

def countChars_big(name):
    name.seek(0)
    tot = 0
    for line in name: tot += len(line)
    return tot

def test_big(name):
    name = open(name)
    return countLines(name), countChars(name)

    

