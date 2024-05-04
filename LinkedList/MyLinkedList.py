class MyLinkedList:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get(self, index: int) -> int:
        count = 0
        current = self
        print(current)
        while current:
            if count == index:
                return current.val
            current = current.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = MyLinkedList(val)
        new_node.next = self
        return new_node

    def addAtTail(self, val: int) -> None:
        new_node = MyLinkedList(val)
        if not self:
            self = new_node
            return
        current = self
        while current.next:
            current = current.next
        current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)
        new_node = MyLinkedList(val)
        count = 0
        current = self
        while current:
            if count == index - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            count += 1
        self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self:
                return self.next
            else:
                return None
        current = self
        prev = None
        count = 0
        while current:
            if count == index:
                if prev:
                    prev.next = current.next
                return
            prev = current
            current = current.next
            count += 1

    def printList(self):
        current = self
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)