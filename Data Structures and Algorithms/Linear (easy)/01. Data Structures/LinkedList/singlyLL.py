# creating a class

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class ListNode:
    def __init__(self, head = None):
        self.head = head

    def printLL(self):
        t = self.head
        while(t.next != None):
            print(t.data, end = " -> ") 
            t = t.next
        print(t.data)

    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
        else: 
            t = self.head
            while(t.next != None):
                t = t.next
            t.next = temp

    def insertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMid(self, value, x):
        temp = Node(value)
        t = self.head

        while(t.next != None):
            if(t.data == x):
                temp.next = t.next
                t.next = temp
            t = t.next

    def delete(self, value):
        t = self.head
        prev = t
        if(t.data == value):
            self.head = self.head.next
        while(t.next != None):
            if(t.data == value):
                prev.next = t.next
                break
            else:
                prev = t
                t = t.next
        if t.data == value:
            prev.next = None

ll = ListNode()
ll.insertAtEnd(10)
ll.insertAtEnd(20)
ll.insertAtEnd(30)
ll.insertAtBeg(5)
ll.insertAtMid(7, 5)
ll.delete(20)

ll.printLL()