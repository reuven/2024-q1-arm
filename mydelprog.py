class MyClass:
    def __init__(self, x):
        self.x = x

    def __del__(self):
        print(f'I am dead {self.x=}')

m1 = MyClass(10)    
m2 = MyClass(20)
m3 = MyClass(30)

