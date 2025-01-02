class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head =None
        self.tail = None
        self.len = 0
    def append(self,node):
        if self.len == 0:
            self.head = node
            self.tail = node
            self.head.next = self.head
            self.head.prev = self.head
            self.len += 1
        else:
            node.prev = self.tail
            node.next = self.head
            self.tail.next = node
            self.head.prev = node
            self.tail = node
            self.len += 1

    def kill(self,index):
        if self.len == 0:
            raise IndexError("index out of range.use one-based indexing.")
        
        if index == 1:
            self.tail.next = self.head.next
            self.head.next.prev = self.tail
            self.head = self.head.next
            self.len -= 1
        elif index == self.len:
            self.head.prev = self.tail.prev
            self.tail.prev.next = self.head
            self.tail = self.tail.prev
            self.len -= 1
        else:
            pointer = self.head
            for j in range(1,index):
                pointer = pointer.next
            pointer.prev.next = pointer.next
            pointer.next.prev = pointer.prev
            self.head = pointer.next
            self.tail = pointer.prev
            self.len -= 1

def josephues(n,k):
    CDLinkedList = LinkedList()
    for i in range(n):
        nodeI = Node(i+1)
        CDLinkedList.append(nodeI)
    while CDLinkedList.len != 1:
        CDLinkedList.kill(k)
    else:
        print(str(CDLinkedList.head.value))
if __name__ == "__main__":
    josephues(7,3)
            