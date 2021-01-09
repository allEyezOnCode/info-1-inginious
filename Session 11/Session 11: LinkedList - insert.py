def insert(self, s):
    node = self.__head
    prev = None
    while node is not None and node.value() < s:
        prev = node
        node = node.next()
    if prev is not None:
        prev_next = prev.next()
        prev.set_next(self.Node(cargo=s, next=prev_next))
    else:
        self.__head = self.Node(cargo=s, next=self.__head)
