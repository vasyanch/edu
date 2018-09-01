class ForErr(Exception):
    logfile = 'formaterror.txt'
    def __init__(self, line, file):
        self.line = line
        self.file = file
    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at', self.file, self.line, file = log)

def parser():
    raise ForErr(40, 'spam.txt')

try:
    parser()
except ForErr as x:
    x.logerror()
