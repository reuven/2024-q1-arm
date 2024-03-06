#!/usr/bin/env python3

import threading
import time
import random
import queue

output = [0]


def hello(n):
    output[0] += n


for i in range(100):
    t = threading.Thread(target=hello, args=(i,), name=f'thread-{i}')
    t.start()

while threading.active_count() > 1:
    for one_thread in threading.enumerate():
        if one_thread != threading.current_thread():
            one_thread.join(0.001)   # non-blocking join

print(output[0])
