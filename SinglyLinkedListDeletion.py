class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # Address of Next Node


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_end(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    def insert_position(self, pos, data):
        np = Node(data)
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

    def display(self):
        if self.head is None:
            print("Single Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next

    def delete_begining(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def delete_position(self, pos):
        prev = self.head
        temp = self.head.next
        for i in range(1, pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next


L = SingleLinkedList()
n1 = Node(10)
L.head = n1
n2 = Node(20)
n1.next=n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
n5 = Node(50)
n4.next = n5

#L.delete_begining()
#L.delete_end()
L.delete_position(0)
L.display()

