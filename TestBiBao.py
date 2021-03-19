
def run():
    a = 2020
    def func():
        nonlocal a
        a = a + 1
        print(a)
        
    return func

if __name__ == '__main__':
    go = run()
    go()
    go()
