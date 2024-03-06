#!/usr/bin/env python3

import threading
import queue

q = queue.Queue()


def file_length(filename):
    total_length = 0

    for one_line in open(filename):
        total_length += len(one_line)

    q.put((filename, total_length))
