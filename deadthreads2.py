#!/usr/bin/env python3

import threading
import time


def long_hello_goodbye():
    print('Hello')
    time.sleep(5)
    print('Goodbye')


def launch_thread():
    print('Start launch')
    t = threading.Thread(target=long_hello_goodbye, daemon=True)
    t.start()
    print('End launch')


print('Running launch_thread')
launch_thread()
print('Done with launch_thread')
