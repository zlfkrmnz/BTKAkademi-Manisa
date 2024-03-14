class Product:
    def __init__(self, product_id, name, price, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description

    def get_details(self):
        return f"""Product ID: {self.product_id}
Name: {self.name}
Price: {self.price}
Description: {self.description}
"""


class WhiteGoods(Product):
    def __init__(self, product_id, name, price, description, brand, model):
        super().__init__(product_id, name, price, description)
        self.brand = brand
        self.model = model

    def get_details(self):
        return f"""{super().get_details()}Brand: {self.brand}
Model: {self.model}
"""


class Fridge(WhiteGoods):
    def __init__(self, product_id, name, price, description, brand, model, capacity, energy_rating, has_freezer):
        super().__init__(product_id, name, price, description, brand, model)
        self.capacity = capacity
        self.energy_rating = energy_rating
        self.has_freezer = has_freezer

    def get_details(self):
        return f"""{super().get_details()}Capacity: {self.capacity}
Energy Rating: {self.energy_rating}
Has Freezer: {self.has_freezer}
"""


class Oven(WhiteGoods):
    def __init__(self, product_id, name, price, description, brand, model, volume, has_self_cleaning):
        super().__init__(product_id, name, price, description, brand, model)
        self.volume = volume
        self.has_self_cleaning = has_self_cleaning

    def get_details(self):
        return f"""{super().get_details()}Volume: {self.volume}
Has self cleaning: {self.has_self_cleaning}
"""
