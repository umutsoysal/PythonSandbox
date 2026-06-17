'''
Spinner Async
'''
import itertools
import math
import time
import asyncio

async def spin(msg: str) -> None:
    for char in itertools.cycle('\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

async def slow() -> int:
    #time.sleep(3)
    #await asyncio.sleep(3)
    is_prime(5000111000222021)  # Example number to check for primality
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
    

async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking!'))
    print('spinner object:', spinner)    
    result = await slow()
    spinner.cancel()
    return result

def main() -> None:
    result = asyncio.run(supervisor())
    print('Answer:', result)

if __name__ == '__main__':    main()