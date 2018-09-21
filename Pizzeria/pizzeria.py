class Pizzeria:
    def __init__(self, order, pizza, booking, order_number, timeout, delivery, delivery_time, contacts, city=None):
        self.order = order
        self.pizza = pizza
        self.booking = booking
        self.order_number = order_number
        self.timeout = timeout
        self.delivery = delivery
        self.delivery_time = delivery_time
        self.contacts = contacts
        self.city = city



    @classmethod
    def import_from_file(cls, pizzeria):
        items_source = open(pizzeria, 'r', encoding='utf-8').readlines()
        items_source = list(map(lambda x: x.replace('\n', '').split(', '), items_source))
        items_schema = items_source.pop(0)
        items_source_as_dict = list(map(lambda x: dict(zip(items_schema, x)), items_source))
        items = []
        for items_dict in items_source_as_dict:
            _items = cls(**items_dict)
            items.append(_items)

        return items


class Pizza(Pizzeria):
    def __init__(self, size, composition, name, price):
        self.size = size
        self.composition = composition
        self.name = name
        self.price = price

    def set_pizza(self, pizza):
        self.pizza = pizza

    def __str__(self):
        return f'Пицца:{self.name} {self.size} см. {self.composition} {self.price} p.'


class Beverages(Pizzeria):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Напитки: {self.name} {self.price} р.'

class Contacts(Pizzeria):
    def __init__(self, Address, Delivery, room):
        self.Address = Address
        self.Delivery = Delivery
        self.room = room

    def __str__(self):
            return f'Контакты : {self.Address} {self.Delivery} {self.room[0]}.'

class Location(Pizzeria):
    def __init__(self, address, Street, city,):
        self.address = address
        self.Street = Street
        self.city = city

    def __str__(self):
        return f'Местоположение: {self.address} {self.Street} {self.city[0]}'
