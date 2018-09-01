#def oops():
#    raise IndexError
def oops():
    raise KeyError

def call_oops():
    try:
        oops()
    except IndexError:
        print('I caught it!')

call_oops()


