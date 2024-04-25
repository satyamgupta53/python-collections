class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __insertAtBegining(self, data) -> None:
        node = Node(data, self.head)
        self.head = node

    def __insertAtEnd(self, data) -> None:
        if self.head is None:
            self.head = Node(data)
            return 
        itr = self.head
        while(itr.next):
            itr = itr.next
        itr.next = Node(data)
        return

    def insert(self, data_list) -> None:
        self.head = None
        for data in data_list:
            self.__insertAtEnd(data)
        return

    def print(self) -> list:
        if self.head is None:
            print("My linked list is empty !") 
            return
        itr = self.head
        ll = ''
        while itr:
            ll += str(itr.data) + ' --> '
            itr = itr.next
        ll += 'None'
        return ll

    def len(self) -> int:
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove(self, idx) -> Node:
        if idx < 0 or idx >= self.len():
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
                break
            itr = itr.next
            count += 1

    def insertAt(self, idx, data):
        if idx < 0 or idx >= self.len():
            raise Exception("Invalid index !")
        if self.head is None:
            print("My linked list is empty !")
            return
        if idx == 0:
            self.__insertAtBegining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert) -> str:
        if self.head is None:
            print("My linked list is empty !")
            return
        itr = self.head
        count = 0
        while itr:
            if itr.data is data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
        return "Inserted at this idx : ", count

    def remove_by_value(self, data):
        if self.head is None:
            print("My linked list is empty !")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.next.data is data:
                itr.next = itr.next.next
                break
            itr = itr.next
        return
        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(['S', 'a', 't', 'y', 'a', 'm'])
    ll.insertAt(3, 'k')
    ll.insert_after_value('k', 'u')
    ll.remove_by_value('u')
    print(ll.print())