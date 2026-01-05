from engine.order_book import OrderBook

class MatchingEngine:
    def __init__(self, order_book):
        self.order_book = order_book
        self.trades = []
    def record_trade(self, price, quantity, buy_order, sell_order, timestamp):
        trade = {
            "price": price,
            "quantity": quantity,
            "buy_order_id": buy_order.order_id,
            "sell_order_id": sell_order.order_id,
            "timestamp": timestamp,
        }
        self.trades.append(trade)
    def process_order(self, order):
        if order.side == "BUY":
            self._process_buy(order)
        elif order.side == "SELL":
            self._process_sell(order)
    def _process_buy(self, buy_order):
        while buy_order.quantity > 0:
            best_ask = self.order_book.get_best_ask()
            if best_ask is None:
                break

            if buy_order.order_type == "LIMIT" and buy_order.price < best_ask.price:
                break

            trade_qty = min(buy_order.quantity, best_ask.quantity)
            trade_price = best_ask.price

            self.record_trade(
                price=trade_price,
                quantity=trade_qty,
                buy_order=buy_order,
                sell_order=best_ask,
                timestamp=buy_order.timestamp,
            )

            buy_order.quantity -= trade_qty
            best_ask.quantity -= trade_qty

            if best_ask.quantity == 0:
                self.order_book.remove_best_ask()

        if buy_order.quantity > 0 and buy_order.order_type == "LIMIT":
            self.order_book.add_order(buy_order)
    def _process_sell(self, sell_order):
        while sell_order.quantity > 0:
            best_bid = self.order_book.get_best_bid()
            if best_bid is None:
                break

            if sell_order.order_type == "LIMIT" and sell_order.price > best_bid.price:
                break

            trade_qty = min(sell_order.quantity, best_bid.quantity)
            trade_price = best_bid.price

            self.record_trade(
                price=trade_price,
                quantity=trade_qty,
                buy_order=best_bid,
                sell_order=sell_order,
                timestamp=sell_order.timestamp,
            )

            sell_order.quantity -= trade_qty
            best_bid.quantity -= trade_qty

            if best_bid.quantity == 0:
                self.order_book.remove_best_bid()

        if sell_order.quantity > 0 and sell_order.order_type == "LIMIT":
            self.order_book.add_order(sell_order)
