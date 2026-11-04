class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

class ListNode:
    def __init__(self, head=None):
        self.head = head

    def printLL(self):
        if not self.head:
            print("Empty List")
            return
        t = self.head
        while t is not None:
            print(t.data, end=" <-> " if t.next else "\n")
            t = t.next

    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = temp
        temp.prev = t

    def insertAtBeg(self, value):
        temp = Node(value)
        if self.head is not None:
            self.head.prev = temp
            temp.next = self.head
        self.head = temp

    def insertAtMid(self, value, x):
        temp = Node(value)
        t = self.head
        while t is not None:
            if t.data == x:
                temp.next = t.next
                temp.prev = t
                if t.next is not None:
                    t.next.prev = temp
                t.next = temp
                return
            t = t.next

    def delete(self, value):
        if self.head is None:
            return

        # Deleting the head node
        if self.head.data == value:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return

        t = self.head
        while t is not None:
            if t.data == value:
                # Update previous node's next
                if t.prev is not None:
                    t.prev.next = t.next
                # Update next node's prev (if not the last node)
                if t.next is not None:
                    t.next.prev = t.prev
                return
            t = t.next

# Test execution:
ll = ListNode()
ll.insertAtEnd(10)
ll.insertAtEnd(20)
ll.insertAtEnd(30)
ll.insertAtBeg(5)
ll.insertAtMid(7, 5)
ll.delete(20)

ll.printLL()
# Expected output: 5 <-> 7 <-> 10 <-> 30