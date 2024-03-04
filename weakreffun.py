import weakref

class MyClass:
    def __init__(self, x):
        self.x = x

    def __del__(self):
        print(f'I am dead {self.x=}')

m1 = MyClass(10)    
m2 = MyClass(20)
m3 = weakref.ref(m1)

print('About to delete m1')
del(m1)
print(f'{m3()=}')

print('About to delete m2')
del(m2)
print(f'{m3()=}')


