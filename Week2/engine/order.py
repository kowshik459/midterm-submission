class Order:
    def __init__(self, order_id, side, price, quantity, timestamp, order_type):
        self.order_id = order_id
        self.side = side
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp
        self.order_type = order_type

    def __repr__(self):
        return (
            f"Order(id={self.order_id}, side={self.side}, "
            f"price={self.price}, qty={self.quantity}, "
            f"time={self.timestamp}, type={self.order_type})"
        )