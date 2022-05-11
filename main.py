from time import time
from problems import *
from test import test


def euler():
    p = p008
    print(f'{p()}\n')
    # test(p)
    # test()


if __name__ == '__main__':
    print()
    start = time()
    euler()
    t = time() - start
    print(f'Completed in {"{:.0f}".format(t * 1000) if t < 1 else "{:.1f}".format(t)}{"m" if t < 1 else ""}s')
