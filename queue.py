class Queue:
    def __init__(self):
        self.li = list()

    def enqueue(self, item):
        self.li.insert(0, item)

    def dequeue(self):
        if len(self.li) != 0:
            return self.li.pop()
        return "Queue is Empty"

    def peek(self):
        if len(self.li) != 0:
            item = self.li.pop()
            self.li.append(item)
            return item
        return "Queue is Empty"

    def is_empty(self):
        if len(self.li) == 0:
            return True
        return False


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(9)
    q.enqueue(8)
    q.enqueue(7)
    print(q.peek())
    print(q.dequeue())
    print(q.is_empty())


