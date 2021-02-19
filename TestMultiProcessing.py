from multiprocessing import Process
from time import sleep
from random import randint

def do_work(work_name):
    print(f"{work_name} started")
    interval = randint(1, 10)
    sleep(interval)
    print(f"{work_name} finished")

def main():
    p1 = Process(target=do_work, args=("Task 1",))
    p2 = Process(target=do_work, args=("Task 2",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("All finished")

if __name__ == '__main__':
    main()