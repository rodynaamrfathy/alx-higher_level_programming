#!/usr/bin/python3
"""
Reads from standard input and computes metrics
"""
import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1

            lines_processed += 1

            if lines_processed % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(status_codes):
                    if status_codes[code] > 0:
                        print("{}: {}".format(code, status_codes[code]))

        except (ValueError, IndexError):
            pass

except KeyboardInterrupt:
    pass

print("File size: {}".format(total_size))
for code in sorted(status_codes):
    if status_codes[code] > 0:
        print("{}: {}".format(code, status_codes[code]))
