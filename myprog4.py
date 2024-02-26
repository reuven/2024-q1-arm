from typing import Optional


def hello(name: None | str = 'whoever') -> str:
    return f'Hello, {name}!'


print(hello(None))
print(hello('world'))
