import heapq

class EventLoop:
    def __init__(self, matching_engine):
        self.engine = matching_engine
        self.current_time = 0
        self.event_queue = []
        self._counter = 0
    def schedule_order(self, timestamp, order):
        heapq.heappush(
            self.event_queue,
            (timestamp, self._counter, order)
        )
        self._counter += 1
    def run(self):
        while self.event_queue:
            timestamp, _, order = heapq.heappop(self.event_queue)
            self.current_time = timestamp
            self.engine.process_order(order)
