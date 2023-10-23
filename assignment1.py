class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    ## insert at the last.
    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode

    ## find the first matched data and delete that node.
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
        print("List: ", end="")
        if not self.head:
            print("Empty List!!")
            return
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print(" ")

    ## 1. Find the length of the linked list.
    def length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    ## 2. Find the middle element of the list.
    def find_middle(self):
        mid_len = self.length() // 2
        middle = self.head
        while mid_len > 0:
            mid_len -= 1
            middle = middle.next
        if not middle:
            return "Empty list. No middle value."
        return middle.data

    ## 3. Delete the last element and add it to the beginning.
    def delete_last_and_add_first(self):
        if not (self.head and self.head.next):
            return
        last_node = self.head
        prev_node = self.head
        while last_node.next:
            prev_node = last_node
            last_node = last_node.next
        prev_node.next = None
        last_node.next = self.head
        self.head = last_node

    ## 4. Display the elements in reverse order.
    def reverse_display(self):
        print("Reverse Display: ", end="")
        if not self.head:
            print("Empty List!!")
            return
        data_list = []
        cur = self.head
        while cur:
            data_list.append(cur.data)
            cur = cur.next
        for i in range(len(data_list) - 1, -1, -1):
            print(data_list[i], end=" ")
        print(" ")

    ## 5. Find the smallest element in the list and delete it.
    def find_smallest_and_delete(self):
        # find smallest
        if not self.head:
            return
        cur = self.head
        smallest = float("inf")
        while cur:
            if cur.data < smallest:
                smallest = cur.data
            cur = cur.next
        # delete smallest
        self.delete(smallest)


## For Testing
linked_list = LinkedList()
linked_list.insert(5)
linked_list.insert(3)
linked_list.insert(7)
linked_list.insert(2)
linked_list.insert(8)
linked_list.print_list()
print(f"Length:{linked_list.length()}")
print(f"Middle:{linked_list.find_middle()}")
linked_list.delete(5)
linked_list.print_list()
print(f"Length:{linked_list.length()}")
print(f"Middle:{linked_list.find_middle()}")
linked_list.delete_last_and_add_first()
linked_list.print_list()
linked_list.reverse_display()
linked_list.insert(10)
linked_list.insert(5)
linked_list.print_list()
linked_list.find_smallest_and_delete()
linked_list.print_list()
