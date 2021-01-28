from turtle import *


def draw(n):
    color('red', 'yellow')
    begin_fill()
    d = 250
    N = 0
    goto(-d / 2, 0)
    while N < n:
        forward(d)
        left(180 + 180 / n)
        N = N + 1
        # if abs(pos()) < 1:
        #    break
    end_fill()
    done()


draw(5)

'''
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)


background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
'''
