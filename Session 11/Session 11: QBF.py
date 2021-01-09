def remove(self, cargo):
    node = self.first()
    if node is not None:
        if node.value() == cargo:
            if self.__first == self.__last:
                self.__first = None
                self.__last = None
                return None
            else:
                self.__first = node.next()
            node.set_next(None)
            return node
        current = self.first()
        while current.next() is not self.first():
            if current.next().value()==cargo:
                if current.next() is self.last():
                    self.__last=current
                    self.__last.set_next(self.first())
                    return node
                current.set_next(current.next().next())
                return node
            current = current.next()
            return None

def removeAll(self, cargo):
    v = self.remove(cargo)
    while v is not None:
        v = self.remove(cargo)
    
                
    
