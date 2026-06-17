import itertools
import time
from threading import Thread, Event


def spin(msg: str, done: Event) -> None:
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

def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=['thinking...', done])
    print('spinner object:', spinner)
    spinner.start()

    result = slow()
    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print('Answer:', result)

if __name__ == '__main__':    main()