def remove(self, cargo):
    node = self.first()
    prev = None
    while node != self.last() and node.value() != cargo:
        prev = node
        node = node.next()
        
    if node is not None and node.value() == cargo:
        if prev is not None:
            if self.last() == node:
                self.__last = prev
            prev.set_next(None)
            node.set_next(None)
            return node
        else:
            if self.first() == self.last():
                self.__first = None
                self.__last = None
                node.set_next(None)
                return node
            else:
                self.__first = self.first().next()
                node.set_next(None)
                return node
            
def removeAll(self, cargo):
    while self.remove(cargo) is not None:
        pass
