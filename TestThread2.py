from threading import Thread, Lock
from time import time, sleep

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()
    
    def deposit(self, amount):
        self._lock.acquire()
        try:
            b = self._balance + amount
            sleep(1)
            self._balance = b
        finally:
            self._lock.release()
            
    @property
    def balance(self):
        return self._balance
    
class DepositThread(Thread):
    def __init__(self, thread_name, account, amount):
        super().__init__()
        self._thread_name = thread_name
        self._account = account
        self._amount = amount
    
    def run(self):
        print(f"{self._thread_name} - Befor - {self._account.balance}\r\n") 
        self._account.deposit(self._amount)
        print(f"{self._thread_name} - After - {self._account.balance}\r\n") 

def main():
    account = Account()
    threads = []
    for i in range(1, 11):
        t = DepositThread(f"t{i}", account,  1)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(account.balance)

if __name__ == '__main__':
    main()