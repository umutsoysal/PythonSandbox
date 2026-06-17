'''
Spinner Process
'''
import itertools
import math
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize

def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle('\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        if done.wait(0.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def slow() -> int:
    time.sleep(3)
    return 42

def is_prime(n: int) -> bool:
    if n <= 2:
        return False
    if n==2:
        return True
    
    if n % 2 == 0:
        return False
    
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True

def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=['thinking!', done])
    print('spinner object:', spinner)
    spinner.start()

    result = is_prime(5000111000222021)  # Example number to check for primality
    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print('Answer:', result)

if __name__ == '__main__':    main()