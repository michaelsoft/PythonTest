import time, threading, random

balance = 0
lock = threading.Lock()

def deposit(amount):
    global balance

    for i in range(10):
        lock.acquire()
        preBalance = balance
        balance += amount
        postBalance = balance
        lock.release()

        print ('Thread %s, %d, %d\n' % (threading.current_thread().name, preBalance, postBalance))
        interval = random.randint(1,3)
        time.sleep(interval)

def withdraw(amount):
    global balance

    #random = Random()

    for i in range(10):
        lock.acquire()
        if (balance > 0) & (balance >= amount) :
            preBalance = balance
            balance -= amount
            postBalance = balance
        lock.release()

        print ('Thread %s, %d, %d\n' % (threading.current_thread().name, preBalance, postBalance))
        interval = random.randint(1,3)
        time.sleep(interval)

depositThread = threading.Thread(target=deposit, args=(100,), name='D')
depositThread.start()
withdrawThread = threading.Thread(target=withdraw, args=(100,), name='W')
withdrawThread.start()

depositThread.join()
withdrawThread.join()

print('Finished...\n')