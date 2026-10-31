# supports FIFO -> first in first out  .... insert from rear and delete from front

class Queue:
    def __init__(self):
        self.q = []

    def isEmpty(self):
        return len(self.q) == 0

    def insert(self, value):
        return self.q.append(value)

    def remove(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else: return self.q.pop(0)

    def front(self):
        return self.q[0]

    def rear(self):
        return self.q[-1]

que = Queue()

print(que.isEmpty())

que.insert(10)
que.insert(20)
que.insert(30)
que.insert(40)

print(que.front())
print(que.rear())

que.remove()
que.remove()
que.remove()

print(que.front())
print(que.rear())

print(que.isEmpty())