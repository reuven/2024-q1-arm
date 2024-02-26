def myfunc(choice):
    if choice == 'a':
        return 'Yay! It is a!'
    elif choice == 'b':
        return 'Boo, it is b!'
    else:
        raise ValueError('Bad value!')
