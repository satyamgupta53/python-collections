class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __insertAtBegining(self, data) -> None:
        if self.head is None:
            self.head = Node(data)
            return
        else:
            node = Node(data, self.head)
            self.head.prev = node
            self.head = node

    def __insertAtEnd(self, data) -> None:
        if self.head is None:
            self.head = Node(data)
            return 
        itr = self.head
        while(itr.next):
            itr = itr.next
        temp = Node(data)
        itr.next = temp
        temp.prev = itr
        return

    def insert(self, data_list) -> None:
        self.head = None
        for data in data_list:
            self.__insertAtEnd(data)
        return

    def len(self) -> int:
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print_forward(self):
        if self.head is None:
            print("My linked list is empty !") 
            return
        itr = self.head
        while itr:
            print(itr.data, end=' --> ')
            itr = itr.next
        print('None')
        return

    def print_backward(self):
        if self.head is None:
            print("My linked list is empty !") 
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        while itr:
            print(itr.data, end=' --> ')
            itr = itr.prev
        print('None')
        return

    def remove(self, idx) -> None:
        if idx < 0 or idx > self.len():
            raise Exception("Invalid index !")
        if self.head is None:
            print("My linked list is empty !")
            return
        if idx == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                break
            itr = itr.next
            count += 1

    def insertAt(self, idx, data):
        if idx < 0 or idx > self.len():
            raise Exception("Invalid Index")
        if idx == 0:
            self.__insertAtBegining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert([1, 2, 3, 4, 5])
    dll.print_forward()
    dll.remove(2)
    dll.print_forward()
    dll.insertAt(2, 3)
    dll.print_forward()
    dll.insertAt(0, 0)
    dll.print_forward()
    dll.insertAt(5, 6)
    dll.print_forward()
    dll.insertAt(7, 7)
    dll.print_forward()
    dll.remove(0)    
    dll.print_forward()


            

    
        