

class Queue:
    def __init__(self, *args):
        self.queue = list(args)

    def add(self, *args):
        self.queue.extend(args)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)

    def __str__(self):
        return " -> ".join(list(map(str, self.queue)))

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


queue1 = Queue(1, 2, 3)
queue2 = Queue(1, 2)

print(queue1 == queue2)
queue2.add(3)
print(queue1 == queue2)