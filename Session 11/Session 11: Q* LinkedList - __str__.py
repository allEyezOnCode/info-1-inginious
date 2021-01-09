def __str__(self):
    node = self.__head
    res = '[ '
    while node is not None:
        res += str(node.value()) + ' '
        node = node.next()
    return res + ']'
