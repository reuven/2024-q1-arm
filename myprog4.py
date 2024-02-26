def hello(name: str = 'whoever'):
    return f'Hello, {name}!'


print(hello())
print(hello('world'))
