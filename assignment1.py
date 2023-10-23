class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next:
            prev = cur
            cur = cur.next
            if cur.data == data:
                prev.next = cur.next
                break
        del cur

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next


linked_list = LinkedList()
linked_list.insert(5)
linked_list.insert(3)
linked_list.insert(7)
linked_list.insert(2)
linked_list.insert(8)

linked_list.delete(5)

linked_list.print_list()
