class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class ListNode:
    def __init__(self, head=None):
        self.head = head

    def printLL(self):
        if not self.head:
            print("Empty List")
            return
        t = self.head
        while True:
            print(t.data, end=" -> ")
            t = t.next
            if t == self.head:
                break
        print(f"(head: {self.head.data})")

    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = temp
            return

        t = self.head
        # Traverse until the last node (the one pointing back to head)
        while t.next != self.head:
            t = t.next
        t.next = temp
        temp.next = self.head

    def insertAtBeg(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = temp
            return

        # Find the tail to update its next pointer to the new head
        t = self.head
        while t.next != self.head:
            t = t.next

        temp.next = self.head
        t.next = temp
        self.head = temp

    def insertAtMid(self, value, x):
        """Inserts value after the node with value x"""
        if self.head is None:
            return

        temp = Node(value)
        t = self.head
        while True:
            if t.data == x:
                temp.next = t.next
                t.next = temp
                return
            t = t.next
            if t == self.head:
                break  # Reached the start again without finding x

    def delete(self, value):
        if self.head is None:
            return

        # Case 1: Deleting head
        if self.head.data == value:
            # If it's the only node in the list
            if self.head.next == self.head:
                self.head = None
                return

            # Find the tail node
            t = self.head
            while t.next != self.head:
                t = t.next
            t.next = self.head.next
            self.head = self.head.next
            return

        # Case 2: Deleting a middle or tail node
        prev = self.head
        curr = self.head.next
        while curr != self.head:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

# Test execution:
ll = ListNode()
ll.insertAtEnd(10)
ll.insertAtEnd(20)
ll.insertAtEnd(30)
ll.insertAtBeg(5)
ll.insertAtMid(7, 5)
ll.delete(20)

ll.printLL()
# Output: 5 -> 7 -> 10 -> 30 -> (head: 5)