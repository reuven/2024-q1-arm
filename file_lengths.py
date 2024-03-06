#!/usr/bin/env python3

import threading
import queue
import glob

q = queue.Queue()


def file_length(filename):
    total_length = 0

    for one_line in open(filename):
        total_length += len(one_line)

    q.put((filename, total_length))


for one_filename in glob.glob('/etc/*.conf'):
    t = threading.Thread(target=file_length, args=(
        one_filename,), name=f'thread-{one_filename}')
    t.start()
