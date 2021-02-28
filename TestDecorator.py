
def func_pwd(func):
    def pwd():
        passwd = input("Pls input the password:")
        if passwd == '123456':
            func()
        else:
            print('Incorrect password')
    return pwd

@func_pwd
def buy():
    print("Buy a stock")

if __name__ == '__main__':
    buy()