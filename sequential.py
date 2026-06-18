"""
Baseline for compparing sequential execution against asynchronous and parallel implementations
"""

from time import perf_counter
from typing import NamedTuple

from chapter19.primes import is_prime

NUMBERS = [10, 29, 87, 97, 101, 113, 127, 131, 197, 199]

class Result(NamedTuple):
    number: int
    elapsed: float

def check(n : int) -> Result:
    t0 = perf_counter()
    prime = is_prime(n)
    return Result(n, perf_counter() - t0)

def main() -> None:
    t0 = perf_counter()
    for n in NUMBERS:
        number, elapsed  = check(n)
        prime = is_prime(n)
        label = "P" if prime else " "
        print(f'{label} Number: {number:16}, Elapsed: {elapsed:.4f} seconds')
    elapsed = perf_counter() - t0
    print(f'Total elapsed time: {elapsed:.4f} seconds')

if __name__ == '__main__':
    main()