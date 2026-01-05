from engine.order import Order
from engine.order_book import OrderBook
from engine.matching_engine import MatchingEngine

ob = OrderBook()
engine = MatchingEngine(ob)

# Add ASK ladder
engine.process_order(Order(1, "SELL", 101, 10, 1, "LIMIT"))
engine.process_order(Order(2, "SELL", 102, 20, 2, "LIMIT"))
engine.process_order(Order(3, "SELL", 103, 30, 3, "LIMIT"))

# MARKET BUY that clears all asks
engine.process_order(Order(4, "BUY", None, 60, 4, "MARKET"))

print("Trades:")
for t in engine.trades:
    print(t)

print("Remaining best ask:", ob.get_best_ask())
