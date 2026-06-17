'''
Spinner Async
'''
import itertools
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
    time.sleep(3)
    #await asyncio.sleep(3)
    return 42

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