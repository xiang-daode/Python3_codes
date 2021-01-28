from turtle import *
import threading
import threading, zipfile

# 线程定义-1:
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

# 线程定义-2:
class AsyncDraw(threading.Thread):
    def __init__(self, inNum, r):
        threading.Thread.__init__(self)
        self.inNum = inNum
        self.r = r

    def run(self):
        color('red', 'yellow')
        begin_fill()
        d = int(self.r)
        N = 0
        n = int(self.inNum)
        goto(-d / 2, 0)
        while N < n:
            forward(d)
            left(180 + 180 / n)
            N = N + 1
            # if abs(pos()) < 1:
            #    break
        end_fill()
        # done()
        print('Finished background  of:', self.inNum)

# =================== 主程序入口 =========================
def main():
    # ============== for Draw  ==================
    background2 = AsyncZip('tutorials_python2.zip', 'tutorials_python3.zip')
    background2.start()
    print('The main program continues to run in foreground.')

    background2.join()  # Wait for the background task to finish
    print('Main program waited until background was done.')

    # ============== for ZIP  ==================
    background = AsyncDraw('5', '180')

    background.start()
    print('The main program continues to run in foreground.')

    background.join()    # Wait for the background task to finish
    print('Main program waited until background was done.')

    # ============== others  ==================
    # draw(5)

main() # 启动主程序








