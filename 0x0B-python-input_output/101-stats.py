#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics.
"""

import sys
import signal

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics(signum, frame):
    """ Print accumulated metrics """
    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_counts):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")
            signal.signal(signal.SIGINT, print_statistics)

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 10:
                file_size = int(parts[-1])
                status_code = int(parts[-2])

                total_file_size += file_size
                status_code_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(None, None)
    except KeyboardInterrupt:
        print_statistics(None, None)
        raise
