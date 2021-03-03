import time
from functools import lru_cache

@lru_cache(maxsize= 5)
def sleeping(coming):
    time.sleep(coming)
    return coming

if __name__ == '__main__':
    sleep = input()

    sleeping(5)
    sleeping(3)
    sleeping(1)
    print("my sleep is coming")

