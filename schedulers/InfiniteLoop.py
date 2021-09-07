import datetime
import time

def do_work():
    #now = datetime.datetime.now
    ts = time.strftime('%Y-%m-%d %H:%M%S', time.localtime())
    print('Working:', ts)

def schedule():
    while (True):
        do_work()
        time.sleep(5)

if __name__ == '__main__':
    schedule()