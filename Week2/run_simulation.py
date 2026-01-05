from engine.order import Order
from engine.order_book import OrderBook
from engine.matching_engine import MatchingEngine
from engine.event_loop import EventLoop

# Initialize components
order_book = OrderBook()
engine = MatchingEngine(order_book)
event_loop = EventLoop(engine)

# Add some orders
event_loop.schedule_order(1, Order(1, "SELL", 101, 10, 1, "LIMIT"))
event_loop.schedule_order(2, Order(2, "SELL", 102, 20, 2, "LIMIT"))
event_loop.schedule_order(3, Order(3, "SELL", 103, 30, 3, "LIMIT"))

event_loop.schedule_order(4, Order(4, "BUY", None, 60, 4, "MARKET"))

# Run simulation
event_loop.run()

# Print trades
print("Trades executed:")
for trade in engine.trades:
    print(trade)
