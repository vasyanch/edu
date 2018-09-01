import sys, traceback

def safe(func, *args):
    try:
        func(*args)
    except:
        traceback.print_exc()
        print(sys.exc_info())
        
import oops
safe(oops.oops)
