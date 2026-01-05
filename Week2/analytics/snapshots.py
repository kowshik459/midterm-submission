class SnapshotRecorder:
    def __init__(self):
        self.snapshots = []

    def record(self, timestamp, best_bid, best_ask):
        if best_bid is not None and best_ask is not None:
            mid_price = (best_bid.price + best_ask.price) / 2
            spread = best_ask.price - best_bid.price
        else:
            mid_price = None
            spread = None

        snapshot = {
            "timestamp": timestamp,
            "best_bid": best_bid.price if best_bid else None,
            "best_ask": best_ask.price if best_ask else None,
            "mid_price": mid_price,
            "spread": spread,
        }

        self.snapshots.append(snapshot)
