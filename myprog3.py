from typing import Literal


def myfunc(choice: Literal['a', 'b']) -> str:
    if choice == 'a':
        return 'Yay! It is a!'
    elif choice == 'b':
        return 'Boo, it is b!'
    else:
        raise ValueError('Bad value!')


print(myfunc('a'))
print(myfunc('b'))
print(myfunc('c'))
