

class Queue:
    def __init__(self, *args):
        self.queue = list(args)

    def add(self, *args):
        self.queue += list(args)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def __str__(self):
        return " -> ".join(map(str, self.queue))

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.queue == other.queue
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(*(self.queue + other.queue))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.queue += other.queue
            return self
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other >= len(self.queue):
                return Queue()
            return Queue(*self.queue[other:])
        return NotImplemented


queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)
