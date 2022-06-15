#!/usr/bin/env python3

import sys

from notebook.auth import passwd


def run():
    args = sys.argv[1:]

    if not args:
        print('Error: Missing password.', file=sys.stderr)
        return

    if password := args[0]:
        encoded = passwd(password)
        print(encoded)
    else:
        print('Error: Empty password.', file=sys.stderr)


if __name__ == '__main__':
    run()
