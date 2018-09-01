def oops():
    raise MyError

class MyError(Exception):
    pass


def call_MyError():
    try:
        oops()
    except (MyError, IndexError) as d:
        print(d.__class__)
    else:
        print("Exception didn't caught")

if __name__ == '__main__':
    call_MyError()

    

