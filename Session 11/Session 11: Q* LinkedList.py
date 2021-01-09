class LinkedList:
    def __init__(self):
        self.__head = None
    def add(self, value):
        self.__head = Node(value, next=self.__head)
    def get_reverse(self):
        node = self.__head
        res = ""
        while node is not None:
            res += node.get_value()
            node = node.next
        return res
class Node:
    def __init__(self, cargo, next=None):
        self.next = next
        self.cargo = cargo
    def get_next(self):
        return self.next
    def get_value(self):
        return self.cargo
        
    
