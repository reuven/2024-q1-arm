#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait
import glob

start_time = time.time()


def file_length(filename):
    total_length = 0

    try:
        for one_line in open(filename):
            total_length += len(one_line)
    except Exception as e:   # never do this!
        print(f'Ignoring {one_filename}: {e}')

    return filename, total_length


with ThreadPoolExecutor() as executor:
    all_results = []
    for one_filename in glob.glob('/etc/*.conf'):
        one_result = executor.submit(file_length, one_filename)
        all_results.append(one_result)

    done, not_done = wait(all_results)

    for one_result in done:
        print(one_result.result())

end_time = time.time()

print(f'Total time: {(end_time - start_time):0.5f}')
