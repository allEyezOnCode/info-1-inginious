def __init__(self, lst):
    self.__length = 0
    self.__head = None
    for el in lst[::-1]:
        self.add(el)
