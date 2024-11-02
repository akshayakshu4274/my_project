# circular_queue.py
class CircularQueue:
    def __init__(self, max_length=5):
        self.queue = {}
        self.max_length = max_length
        self.current_index = 0
    
    def enqueue(self, element):
        self.queue[self.current_index] = element
        self.current_index += 1
        if len(self.queue) > self.max_length:
            oldest_index = min(self.queue.keys())
            del self.queue[oldest_index]
    
    def display(self):
        return list(self.queue.values())

