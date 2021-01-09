__prochain_numero = 1
def __init__(self):
    self.__numero = self.get_numero()
    self.increment()
@classmethod
def increment(cls):
    cls.__prochain_numero += 1
@classmethod
def get_numero(cls):
    return cls.__prochain_numero
