class MyLinkedList:

    def __init__(self,val =0  ,next = None):
        self.val = val
        self.next = next

    def get(self, index: int) -> int:
        count = 0
        
        while self:
            if count == index:
                return self.val
            self = self.next
            count += 1
        
        return -1

    # def addAtHead(self, val: int) -> None:
        

    # def addAtTail(self, val: int) -> None:
        

    # def addAtIndex(self, index: int, val: int) -> None:
        

    # def deleteAtIndex(self, index: int) -> None:
