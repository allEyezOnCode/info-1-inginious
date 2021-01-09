class Student:
    __id = 0
    def __init__(self, firstname, surname, birthday, email):
        self.firstname = firstname
        self.surname = surname
        self.birthday = birthday
        self.email = email
        self.id = self.new_id()
    def __str__(self):
        return f"Student number {self.id}: {self.firstname} {self.surname} born the {self.birthday}, can be reached at {self.email}"
    @classmethod
    def new_id(cls):
        id_ = cls.__id
        cls.__id += 1
        return id_
