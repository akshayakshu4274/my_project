from circular_queue import CircularQueue

def test_circular_queue():
    cq = CircularQueue(max_length=3)
    cq.enqueue("A")
    cq.enqueue("B")
    cq.enqueue("C")
    cq.enqueue("D")
    assert cq.display() == ["B", "C", "D"]

