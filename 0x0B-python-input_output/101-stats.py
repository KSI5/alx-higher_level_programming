#!/usr/bin/python3

import sys

def print_stats(size, status_codes):
    """
    Print accumulated metrics.

    Args:
        size (int): The accumulated file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for code in sorted(status_codes):
        count = status_codes[code]
        print("{}: {}".format(code, count))

if __name__ == "__main__":
    size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            components = line.split()
            if len(components) >= 2:
                status_code = components[-2]
                file_size = components[-1]

                if status_code in status_codes:
                    status_codes[status_code] += 1

                try:
                    size += int(file_size)
                except ValueError:
                    pass

            if line_count % 10 == 0:
                print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
