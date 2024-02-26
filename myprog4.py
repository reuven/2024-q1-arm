from typing import Optional


def hello(name: Optional[str] = 'whoever') -> str:
    return f'Hello, {name}!'


print(hello(None))
print(hello('world'))
