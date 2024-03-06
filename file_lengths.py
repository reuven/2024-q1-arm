#!/usr/bin/env python3

import threading
import queue
import glob

q = queue.Queue()


def file_length(filename):
    total_length = 0

    try:
        for one_line in open(filename):
            total_length += len(one_line)
    except Exception as e:   # never do this!
        print(f'Ignoring {one_filename}: {e}')

    q.put((filename, total_length))


for one_filename in glob.glob('/etc/*.conf'):
    t = threading.Thread(target=file_length, args=(
        one_filename,), name=f'thread-{one_filename}')
    t.start()

while threading.active_count() > 1:
    for one_thread in threading.enumerate():
        if one_thread != threading.current_thread():
            one_thread.join(0.001)

while not q.empty():
    print(q.get())
