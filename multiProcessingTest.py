import os
from multiprocessing import Process

def doWork():
    x = 0
    while x < 10:
        x += 1
        print('%d' % x)

if __name__ == '__main__':
    p = Process(target=doWork)
    p.start()
    p.join()

    print('Finished...')