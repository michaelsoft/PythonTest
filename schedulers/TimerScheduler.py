import datetime
import time
from threading import Timer

def do_work():
    #now = datetime.datetime.now
    ts = time.strftime('%Y-%m-%d %H:%M%S', time.localtime())
    print('Working:', ts)
    set_timer()

def set_timer():
    t = Timer(5, do_work)
    t.start()

if __name__ == '__main__':
    set_timer()