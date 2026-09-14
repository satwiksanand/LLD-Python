from abc import ABC, abstractmethod


# 1. The Abstraction (Interface)
# This defines the contract that all payment processors must follow.
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# 2. Low-Level Modules (Details)
# These classes implement the abstraction.
class StripeProcessor(PaymentProcessor):
    def pay(self, amount: float) -> None:
        print(f"Processing ${amount:.2f} via Stripe 💳")


class PayPalProcessor(PaymentProcessor):
    def pay(self, amount: float) -> None:
        print(f"Processing ${amount:.2f} via PayPal 💸")


# 3. High-Level Module
# It depends on the abstraction (PaymentProcessor), not the concrete classes.
class Store:
    def __init__(self, payment_processor: PaymentProcessor):
        # We inject the dependency here.
        self.payment_processor = payment_processor

    def purchase_item(self, item_name: str, price: float) -> None:
        print(f"Item '{item_name}' purchased.")
        # The Store doesn't care HOW the payment is processed, just that it has a .pay() method.
        self.payment_processor.pay(price)


# 4. Usage (Dependency Injection)
if __name__ == "__main__":
    # We can easily swap Stripe for PayPal without changing the Store class.

    stripe_api = StripeProcessor()
    my_store = Store(payment_processor=stripe_api)
    my_store.purchase_item("Laptop", 1200.00)

    print("\nSwapping payment gateway...")

    paypal_api = PayPalProcessor()
    my_store_eu = Store(payment_processor=paypal_api)
    my_store_eu.purchase_item("Headphones", 150.00)