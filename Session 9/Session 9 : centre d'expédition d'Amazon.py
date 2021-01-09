class Command:
    sold = 0
    total_price = 0
    def __init__(self, id_buyer, id_item, quantity, price):
        self.id_buyer = id_buyer
        self.id_item = id_item
        self.quantity = quantity
        self.price = price
        self.increase_cmd()
        self.increase_total_price(price * quantity)
    @classmethod
    def increase_cmd(cls):
        cls.sold += 1
    @classmethod
    def increase_total_price(cls, price):
        cls.total_price += (price)
        
    def get_price(self):
        return self.price
    def __str__(self):
        return f"{self.id_buyer}, {self.id_item} : {self.price} * {self.quantity} = {self.price * self.quantity}"
    @classmethod
    def get_number_total_command(cls):
        return cls.sold
    @classmethod
    def get_total_price(cls):
        return cls.total_price
