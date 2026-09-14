# The Single Responsibility Principle says that a class should have
# one and only one reason to change.
#
# If a class has more than one reason to change,
# then it will be harder to test and maintain.


# BAD DESIGN
#
# ShoppingCart is responsible for:
# 1. Maintaining the cart
# 2. Making payments
#
# These are two different responsibilities.

class ShoppingCart:
    def __init__(self):
        self._cart: list[dict] = []

    def add_item(self, name: str, quantity: int):
        self._cart.append({
            "name": name,
            "quantity": quantity
        })

    def make_payment(self):
        print(
            f"Make a payment of "
            f"{sum(item['quantity'] for item in self._cart)}"
        )

    def checkout(self):
        self.make_payment()


# GOOD DESIGN
#
# ShoppingCart is responsible only for managing the cart.
# PaymentProcessor is responsible only for payments.


class ShoppingCart2:
    def __init__(self):
        self._cart: list[dict] = []

    def add_item(self, name: str, quantity: int):
        self._cart.append({
            "name": name,
            "quantity": quantity
        })

    def get_total_quantity(self) -> int:
        return sum(
            item["quantity"]
            for item in self._cart
        )

    def get_items(self) -> list[dict]:
        return self._cart


class PaymentProcessor:
    def make_payment(self, amount: int):
        print(f"Make a payment of {amount}")


class CheckoutService:
    def __init__(self, payment_processor: PaymentProcessor):
        self._payment_processor = payment_processor

    def checkout(self, cart: ShoppingCart2):
        amount = cart.get_total_quantity()
        self._payment_processor.make_payment(amount)


cart = ShoppingCart2()

cart.add_item("Laptop", 1)
cart.add_item("Mouse", 2)

payment_processor = PaymentProcessor()

checkout = CheckoutService(payment_processor)

checkout.checkout(cart)