def hello(name: str = 'whoever') -> str:
    return f'Hello, {name}!'


print(hello())
print(hello('world'))
