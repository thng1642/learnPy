# The towers of Hanoi
# Three towers stand tall. We will label A, B and C.
# Doughnut-shape discs are around tower A, follow top --> bottom is narrowest to widest.
# Following constraints:
# 1. Only one disc can be moved at a time
# 2. The topmost disc of any tower is the only on available for moving.
# 3. A wider disc can never be atop a narrower disc.

from typing import TypeVar, Generic, List
T=TypeVar('T')

class Stack(Generic[T]):
    def __init__(self, name) -> None:
        self._container: List[T] = []
        self._name: str = name
    
    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.pop()
    
    # explore the contents of towers. __repr()__ is what will be output when print() is applied to a Stack.
    def __repr__(self) -> str:
        return repr(f'{self._name}: {self._container}')

# Solving The Tower of Hanoi
# Have 2 scenarios:
# 1. Moving one disc (the base case).
# 2. Moving more than one disc (the recursive case).
# --------------///\\\--------------
# We could break the recursive case into three steps:
# 1. Move the upper n-1 discs from tower A to B (the temporary tower), using C as the in-between. Implement hanoi(begin, tmp, end, n-1).
# 2. Move the single lowest disc from A to C. Implement hanoi(begin, end, tmp, 1).
# 3. Move n-1 discs from tower B to C, using A as the in-between. Implement hanoi(tmp, end, begin, n-1).

def hanoi(begin: Stack[int], end: Stack[int], tmp: Stack[int], n: int)->None:
    if n == 1:
        end.push(begin.pop())

        towers = [begin, end, tmp]
        for item in towers:
            if item._name == 'A':
                print(item)
        for item in towers:        
            if item._name == 'B':
                print(item)
        for item in towers:
            if item._name == 'C':
                print(item)
        print('\n------===------\n')

        # print(begin)
        # print(end)
        # print(tmp)
        # print('\n------===------\n')
    else: 
        hanoi(begin, tmp, end, n - 1)
        hanoi(begin, end, tmp, 1)
        hanoi(tmp, end, begin, n - 1)

if __name__ == "__main__": 
    num_discs:int = 3
    tower_a:Stack[int] = Stack('A')
    tower_b:Stack[int] = Stack('B')
    tower_c:Stack[int] = Stack('C')
    
    for i in range(1, num_discs + 1):
        tower_a.push(i)

    hanoi(tower_a, tower_c, tower_b, num_discs)
    # chạy thuật toán bằng tay đc mô tả trong file hanoi.png