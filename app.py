from LinkedList.MyLinkedList import MyLinkedList

my_list = MyLinkedList(1)
my_list.next = MyLinkedList(2)
my_list.next.next = MyLinkedList(3)

print(my_list.get(1))