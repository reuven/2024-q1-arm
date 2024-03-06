#!/usr/bin/env python3

import multiprocessing
import glob
import time

start_time = time.time()

q = multiprocessing.Queue()


def file_length(filename):
    total_length = 0

    try:
        for one_line in open(filename):
            total_length += len(one_line)
    except Exception as e:   # never do this!
        print(f'Ignoring {one_filename}: {e}')

    q.put((filename, total_length))


all_processes = []
for one_filename in glob.glob('/etc/*.conf'):
    p = multiprocessing.Process(target=file_length, args=(
        one_filename,), name=f'proc-{one_filename}')
    all_processes.append(p)
    p.start()

for one_process in all_processes:
    one_process.join()

while not q.empty():
    print(q.get())

end_time = time.time()

print(f'Total time: {(end_time - start_time):0.5f}')
