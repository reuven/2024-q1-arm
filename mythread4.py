#!/usr/bin/env python3

import threading
import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'{n} Hello!')


for i in range(10):
    t = threading.Thread(target=hello, args=(i,), name=f'thread-{i}')
    t.start()

print('Done!')

for one_thread in threading.enumerate():
    if one_thread != threading.current_thread():
        one_thread.join()
        print(f'\nJoining {one_thread.name}')

print('Starting something new')
