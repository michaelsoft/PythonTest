from threading import Thread
from time import time, sleep
from random import randint

def do_work(name):
    print(f"{name} started")
    val = randint(5, 10)
    sleep(val)
    print(f"{name} finished")

def main():
    t1 = Thread(target=do_work, args=("Task 1",))
    t2 = Thread(target=do_work, args=("Task 2",))
    t1.start()
    t2.start()
    t1.join()
    t2.join
    print("All finished")

if __name__ == "__main__":
    main()