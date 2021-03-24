class BaseProcessor:
    def __init__(self, val):
        super().__init__()
        self.__val = val

    def main(self):
        print(f"Value in base = {self.__val}")
        self.do_work1()
        self.do_work2()
        self.do_work3()
    
    def do_work1(self):
        print("Doing work 1")

    def do_work2(self):
        pass

    def do_work3(self):
        print("Doing work 3")

class ChildProcessor(BaseProcessor):
    def __init__(self, val, val2):
        super().__init__(val)
        # print(f"Value in child = {self.val}")

    def do_work2(self):
        print("Doing work 2 in ChildProcessor")


p = ChildProcessor(10, 'abc')
p.main()

