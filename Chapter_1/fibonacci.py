from typing import Dict, Generator
from functools import lru_cache

# memoization to the rescue
memo: Dict[int, int] = {0:0, 1:1}
def fib1(n:int) -> int:
    if n not in memo:
        memo[n] = fib1(n - 1) + fib1(n - 2)
    return memo[n]

# sample with fib1 memoization    
@lru_cache(maxsize=None) # no limit
def fib2(n:int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)

# Generating Fibonacci 
def fib3(n:int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

# The Fibonacci sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
def fibonacci(n:int) -> int:
    if n <= 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__ == '__main__':
    # print(fibonacci(50))
    # print(fib1(50))

    for i in fib3(6):
        print(i)