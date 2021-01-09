class Node:
    def __init__(self, s, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.value = s
    def get_text(self):
        return self.value
    def set_text(self, s):
        self.value = s
class Tape:
    def __init__(self):
        self.current = None
        self.length = 0
    def next(self):
        if self.current.next is not None:
            self.current = self.current.next
            return self.current.get_text()
    def previous(self):
        if self.current.prev is not None:
            self.current = self.current.prev
            return self.current.get_text()
    def get_length(self):
        return self.length
    def add(self, s):
        self.length += 1
        if self.current is None:
            self.current = Node(s)
        else:
            node = self.current
            prev = None
            while node is not None:
                prev = node
                node = node.next
            prev.next = Node(s, prev=prev)
    def write(self, s):
        self.current.set_text(s)
    def read(self):
        if self.current is not None:
            return self.current.get_text()
