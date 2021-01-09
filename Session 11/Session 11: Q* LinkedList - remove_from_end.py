def remove_from_end(self):
    node = self.__head
    if node is not None:
        self.__length -= 1
        if node.next() is None:
            self.__head = None
        else:
            while node.next().next() is not None:
                node = node.next()
            node.set_next(None)
