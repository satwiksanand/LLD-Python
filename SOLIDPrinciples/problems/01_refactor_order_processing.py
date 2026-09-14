# Task: break up this God class while keeping the public API and outputs identical (Single Responsibility).
# - InventoryManager: owns the stock map, availability checks, and stock updates.
# - NotificationService: owns confirmation formatting and the message history.
# - OrderProcessor: validation, pricing, order IDs, and workflow coordination.
# - Give OrderProcessor an __init__ that accepts an InventoryManager and a NotificationService,
#   and keep the no-argument form that builds defaults for the judge.
# Rejected orders must not change stock, consume an order ID, or record a confirmation.

class BadOrderProcessor:
    def __init__(self):
        self._stock = {"LAPTOP": 10, "PHONE": 25, "TABLET": 15}
        self._messages = []
        self._order_counter = 0

    def _valid_email(self, email: str) -> bool:
        at = email.find("@")
        return 0 < at < len(email) - 1

    def _unit_price(self, product_id: str) -> float:
        return {
            "LAPTOP": 1000.0,
            "PHONE": 500.0,
            "TABLET": 300.0,
        }.get(product_id, 0.0)

    def placeOrder(
        self, productId: str, quantity: int, customerEmail: str
    ) -> str:
        if not productId or quantity <= 0 or not self._valid_email(customerEmail):
            return "INVALID_ORDER"
        available = self._stock.get(productId, 0)
        if available < quantity:
            return "OUT_OF_STOCK"

        self._stock[productId] = available - quantity
        self._order_counter += 1
        order_id = f"ORD-{self._order_counter}"
        total = self._unit_price(productId) * quantity
        self._messages.append(
            f"EMAIL {customerEmail} | {order_id} confirmed | total ${total:.2f}"
        )
        return order_id

    def stockOf(self, productId: str) -> int:
        return self._stock.get(productId, 0)

    def orderCount(self) -> int:
        return self._order_counter

    def confirmations(self) -> list[str]:
        return list(self._messages)

# Good Design

class InventoryManager:
    def __init__(self):
        self._stock = {"LAPTOP": 10, "PHONE": 25, "TABLET": 15}
        self._item_prices = {"LAPTOP": 1000.0, "PHONE": 500.0, "TABLET": 300.0}

    def unit_price(self, product_id: str) -> float:
        return self._item_prices.get(product_id, 0.0)

    def stock_of(self, product_id: str) -> int:
        return self._stock.get(product_id, 0)

    def update_item_quantity(self, product_id: str, quantity: int):
        if product_id not in self._stock and self._stock.get(product_id, 0) - quantity < 0:
            return
        self._stock[product_id] -= quantity

class NotificationService:
    def __init__(self):
        self._messages = []

    def confirmations(self) -> list[str]:
        return list(self._messages)

    def add_message(self, order_id: str, total_price: float, customer_email: str):
        self._messages.append(f"EMAIL {customer_email} | {order_id} confirmed | total ${total_price:.2f}")

class OrderProcessor:
    def __init__(self, inventory_manager = None, notification_service = None):
        self._notification_service = (
            notification_service if notification_service is not None else NotificationService()
        )
        self._inventory_manager = (
            inventory_manager if inventory_manager is not None else InventoryManager()
        )
        self._order_counter = 0

    def _valid_email(self, email: str) -> bool:
        at = email.find("@")
        return 0 < at < len(email) - 1

    def _unit_price(self, product_id: str):
        return self._inventory_manager.unit_price(product_id)

    def orderCount(self) -> int:
        return self._order_counter

    def placeOrder(self, product_id: str, quantity: int, customer_email: str) -> str:
        if not product_id or quantity <= 0 or not self._valid_email(customer_email):
            return "INVALID_ORDER"
        if self._inventory_manager.stock_of(product_id) < quantity:
            return "OUT_OF_STOCK"
        self._inventory_manager.update_item_quantity(product_id, quantity)
        self._order_counter += 1
        total = self._inventory_manager.unit_price(product_id) * quantity
        order_id = f"ORD-{self._order_counter}"
        self._notification_service.add_message(order_id, total, customer_email)
        return order_id

    def confirmations(self):
        return self._notification_service.confirmations()

    def stockOf(self, product_id: str):
        return self._inventory_manager.stock_of(product_id)

if __name__ == "__main__":
    orders = OrderProcessor()
    orders.placeOrder("LAPTOP", 2, "whatisthis@what.com")
    orders.placeOrder("PHONE", 1, "someone@outlook.com")
    print(orders.confirmations())
