from multiprocessing import Process

counter = 0

def sub_task(name):
    global counter
    while counter < 10:
        print(f"Doing {name} for {counter} time", flush=True)
        counter += 1

def main():
    p1 = Process(target=sub_task, args=("Task 1",))
    p2 = Process(target=sub_task, args=("Task 2",))
    p1.start()
    p2.start()

if __name__ == '__main__':
    main()
