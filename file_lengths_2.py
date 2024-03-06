#!/usr/bin/env python3

import threading
import queue
import glob
import time

start_time = time.time()

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
    file_length(one_filename)

while not q.empty():
    print(q.get())

end_time = time.time()

print(f'Total time: {(end_time - start_time):0.5f}')
