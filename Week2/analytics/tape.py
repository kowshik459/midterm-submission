class TradeTape:
    def __init__(self):
        self.trades = []

    def record(self, trade):
        self.trades.append(trade)
