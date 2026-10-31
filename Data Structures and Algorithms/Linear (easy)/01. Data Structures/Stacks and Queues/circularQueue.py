class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.__cq = [None] * size
        self.front = self.rear = -1

    def insert(self, value):
        if ((self.rear + 1) % self.size == self.front):
            raise Exception("Queue is full")
        elif (self.front == -1):
            self.front = self.rear = 0
            self.__cq[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.__cq[self.rear] = value

    def delete(self):
        if self.front == -1:
            raise Exception("Queue is Empty")
        elif self.front == self.rear:
            print(self.__cq[self.front], "is deleted")
            self.front = self.rear = -1
        else:
            print(self.__cq[self.front], "is deleted")
            self.front = (self.front + 1) % self.size

cq = CircularQueue(5)

cq.insert(10)
cq.insert(20)
cq.insert(30)
cq.insert(40)
cq.insert(50)

cq.delete()
cq.delete()
