class MinStack:
    _stack = []
    _minStack = []
    _size = 0

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        if len(self._stack) == self._size:
            self._stack.append(0)
            self._minStack.append(0)
        
        self._stack[self._size] = val
        
        if self._size == 0:
            self._minStack[self._size] = val
        else:
            self._minStack[self._size] = min(val, self.getMin())
        self._size += 1

    def pop(self) -> None:
        self._size -= 1

    def top(self) -> int:
        return self._stack[self._size - 1]

    def getMin(self) -> int:
        return self._minStack[self._size - 1]
