"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import time


def scheduler(n, f, tuple=None):
    time.sleep(n / 100)  # looks for seconds not milli-seconds
    try:
        f(tuple)
    except:
        f()


def f():
    print("We are in F")


def main():
    scheduler(10, f)
    scheduler(100, f)


if __name__ == "__main__":
    main()
