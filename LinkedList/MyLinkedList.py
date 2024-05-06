class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.length = 0
        self.dummy = Node(0)

    def get(self, index: int) -> int:
        count = 0
        current = self.dummy
        while current:
            if count == index:
                return current.val
            current = current.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
       if self.length < 1:
            self.dummy = Node(val)
            self.length += 1
            return
       current = self.dummy
       self.dummy = Node(val)
       self.dummy.next = current
       self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.length < 1:
            self.dummy = Node(val)
            self.length += 1
            return
        new_node = Node(val)
        current = self.dummy
        while current.next:
            current = current.next
        current.next = new_node
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)
        new_node = Node(val)
        count = 0
        current = self.dummy
        while current:
            if count == index - 1:
                new_node.next = current.next
                current.next = new_node
                self.length += 1
                return
            current = current.next
            count += 1
        self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        if index == 0:
            if self.dummy.next:
                self.dummy.next = self.dummy.next.next
                self.length -= 1
            return
        current = self.dummy.next
        prev = self.dummy  # Set prev to dummy node initially
        count = 0        
        while current:
            if count == index:
                prev.next = current.next
                self.length -= 1  
                return
            prev = current
            current = current.next
            count += 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
