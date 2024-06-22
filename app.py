from LinkedList.MyLinkedList import MyLinkedList

my_list = MyLinkedList()
# my_list = MyLinkedList(2)  

# print(my_list.val)
# my_list.next.next = MyLinkedList(3)
my_list.addAtHead(1)
my_list.addAtTail(3)
my_list.addAtIndex(1,2)
# my_list.deleteAtIndex(2)

# my_list.get(2)
print(my_list.get(0))
print(my_list.get(1))
print(my_list.get(2))

print(my_list.get(3))
print(my_list.get(4))
      

