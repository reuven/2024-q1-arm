def myfunc(choice: str) -> str:
    if choice == 'a':
        return 'Yay! It is a!'
    elif choice == 'b':
        return 'Boo, it is b!'
    else:
        raise ValueError('Bad value!')


print(myfunc('a'))
print(myfunc('b'))
