import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
    return wrapper

class Orders:
    id: str = ""
    _items_: list[dict] = []
    __recipient_name: str
    __recipient_contact: str

    def __init__(self, order_id, items):
        self.id = order_id
        self._items = items

    @property
    def recipient_name(self):
        return self.__recipient_name

    @property
    def recipient_contact(self):
        return self.__recipient_contact

    @recipient_name.setter
    def recipient_name(self, value):
        self.__recipient_name = value

    @recipient_contact.setter
    def recipient_contact(self, value):
        self.__recipient_contact = value


    @property
    def items(self):
        return self._items

    @measure_time
    def process_order(self):
        time.sleep(1)

if __name__ == "__main__":
    order = Orders("sei37ask", [{"apples": 20}])
    print(order.id)
    print(order.items)
    print(order.__dict__["_items"])
    order.process_order()
    order.recipient_name = "xyz"
    order.recipient_contact = "90385987349"
    print(order.recipient_name)
    print(order.recipient_contact)
