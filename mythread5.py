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

while threading.active_count() > 1:
    for one_thread in threading.enumerate():
        if one_thread != threading.current_thread():
            one_thread.join(0.001)   # non-blocking join
            if one_thread.is_alive():
                print(f'\nFailed to join {one_thread.name}; will return to it')
            else:
                print(f'\nJoined {one_thread.name}')

print('Starting something new')
