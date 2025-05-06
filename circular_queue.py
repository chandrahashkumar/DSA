class CircularQueue:
    """A circular queue implementation using a fixed-size array."""

    def __init__(self, capacity):
        """Initialize an empty circular queue with given capacity.

        Args:
            capacity (int): The maximum number of elements the queue can hold
        """
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0

    def is_empty(self):
        """Check if the queue is empty.

        Returns:
            bool: True if queue is empty, False otherwise
        """
        return self.size == 0

    def is_full(self):
        """Check if the queue is full.

        Returns:
            bool: True if queue is full, False otherwise
        """
        return self.size == self.capacity

    def enqueue(self, item):
        """Add an item to the rear of the queue.

        Args:
            item: The item to be added to the queue

        Returns:
            bool: True if successful, False if queue is full
        """
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return False

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item
        self.size += 1
        return True

    def dequeue(self):
        """Remove and return the item at the front of the queue.

        Returns:
            The item at the front of the queue, or None if queue is empty
        """
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None

        item = self.queue[self.front]

        if self.front == self.rear:  # Last item in queue
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        self.size -= 1
        return item

    def peek(self):
        """Return the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue, or None if queue is empty
        """
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def display(self):
        """Display all elements in the queue."""
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Queue contents:", end=" ")
        index = self.front
        count = 0

        while count < self.size:
            print(self.queue[index], end=" ")
            index = (index + 1) % self.capacity
            count += 1
        print()


# Example usage
if __name__ == "__main__":
    # Create a circular queue with capacity 5
    cq = CircularQueue(5)

    # Test enqueue operations
    print("Enqueuing items 1, 2, 3, 4, 5:")
    for i in range(1, 6):
        cq.enqueue(i)
    cq.display()

    # Test dequeue operations
    print("\nDequeuing two items:")
    print("Dequeued:", cq.dequeue())
    print("Dequeued:", cq.dequeue())
    cq.display()

    # Test enqueueing after dequeuing
    print("\nEnqueuing 6 and 7:")
    cq.enqueue(6)
    cq.enqueue(7)
    cq.display()

    # Test peek operation
    print("\nPeek at front item:", cq.peek())

    # Test full queue
    print("\nTrying to enqueue to full queue:")
    cq.enqueue(8)

    # Dequeue all remaining items
    print("\nDequeuing all items:")
    while not cq.is_empty():
        print("Dequeued:", cq.dequeue())

    # Test empty queue
    print("\nTrying to dequeue from empty queue:")
    cq.dequeue()