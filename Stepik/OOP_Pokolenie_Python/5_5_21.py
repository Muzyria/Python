class Queue:
    def __init__(self, *args):
        self.queue = list(args)

    def add(self, *args):
        self.queue.extend(list(args))

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def __str__(self):
        return ' -> '.join(map(str, self.queue))

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.queue == other.queue
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Queue):
            res = self.queue + other.queue
            return Queue(*res)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.queue.extend(other.queue)
            return self
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other >= len(self.queue):
                return Queue()
            else:
                return Queue(*self.queue[other::])
        return NotImplemented


queue = Queue(1, 2, 3, 4, 5)

print(queue >> 0)
