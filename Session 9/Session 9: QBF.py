class CD(Item):
    __serial = 99999
    def __init__(self, author, title, time):
        super().__init__(author, title, self.new_serial())
        self.__author = author
        self.__title = title
        self.time = time
    def __str__(self):
        return "[{}] {}, {} ({} s)".format(self.__serial,self.__author,self.__title, self.time)
    @classmethod
    def new_serial(cls):
        serial = cls.__serial
        cls.__serial += 1
        return serial
