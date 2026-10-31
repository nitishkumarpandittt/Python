# we can insert and delete elements from both ends

class Deque:
    def __init__(self):
        self.__dq = []

    def isEmpty(self):
        return len(self.dq) == 0

    def insertAtEnd(self, value):
        return self.dq.append(value)
    
    def insertAtFront(self, value):
        return self.dq.insert(0, value)

    def removeFromEnd(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else: return self.dq.pop()
    
    def removeFromFront(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else: return self.dq.pop(0)

    def front(self):
        print(self.dq[0])

    def rear(self):
        print(self.dq[-1])

dq = Deque()


dq.insertAtEnd(10)
dq.insertAtEnd(20)

dq.front()
dq.rear()
print()

dq.insertAtFront(30)
dq.insertAtEnd(40)

dq.front()
dq.rear()
print()

dq.removeFromFront()
dq.removeFromEnd()

dq.front()
dq.rear()
print()
