class People:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"{self.name} is moving...")

def main():
    p = People("Michael")
    print(p.name)
    p.move()

if (__name__ == '__main__'):
    main()
    