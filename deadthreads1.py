#!/usr/bin/env python3

import threading
import time


def long_hello_goodbye():
    print('Hello')
    time.sleep(5)
    print('Goodbye')


def launch_thread():
    t = threading.Thread(target=long_hello_goodbye)
    t.start()


print('Running launch_thread')
print('Done with launch_thread')
