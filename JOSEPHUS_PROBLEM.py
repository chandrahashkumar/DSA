'''
Josephus Problem
The Josephus problem is a theoretical problem related to a certain elimination game:

n people stand in a circle.

Every k-th person is eliminated in each step.

The last remaining person is the survivor.
'''

# Node class for the circular linked list
class Node:
    def __init__(self, data):
        """
        Initializes a node with given data and a pointer to the next node.
        """
        self.data = data  # Stores the person's position in the circle
        self.next = None  # Pointer to the next node

# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        """
        Initializes an empty circular linked list.
        """
        self.head = None  # Head node of the circular list

    def append(self, data):
        """
        Adds a new node at the end of the circular linked list.
        """
        new_node = Node(data)  # Create a new node

        if not self.head:
            # If list is empty, the new node ktpoints to itself
            self.head = new_node
            self.head.next = self.head
        else:
            # Insert at the end by traversing to the last node
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  # Point new node back to head

    def josephus(self, k):
        """
        Solves the Josephus problem for a given k-step elimination.
        Returns the position of the last remaining person.
        """
        temp = self.head

        # If the list is empty, return None
        if not temp:
            return None

        # Traverse until only one node is left
        while temp.next != temp:
            # Move `k-1` times (since we eliminate the k-th person)
            for _ in range(k - 1):
                temp = temp.next  # Move to the next node

            # Remove the k-th person
            print(f"Eliminating: {temp.next.data}")
            temp.next = temp.next.next  # Skip the eliminated node

        # The last remaining node is the survivor
        return temp.data



# Create a circular linked list and add people (positions 1 to 7)
cll = CircularLinkedList()
for i in range(1, 8):  # 7 people in the circle
    cll.append(i)

# Solve the Josephus problem with k = 3 (every 3rd person is eliminated)
survivor = cll.josephus(2)
print(f"The survivor is at position: {survivor}")


'''
Step-by-Step Execution
Initial Circular Linked List
Person	Next
1    →	  2
2    →	  3
3    →	  4
4    →	  5
5    →	  6
6    →	  7
7    →	  1
Elimination Process (k=3)
Step	Current Position	Eliminated Person	Remaining Circle
1	Start at 1	                 3	       (1 → 2 → 4 → 5 → 6 → 7 → 1)
2	Move to 4	                 6	       (1 → 2 → 4 → 5 → 7 → 1)
3	Move to 7	                 2	       (1 → 4 → 5 → 7 → 1)
4	Move to 5	                 1	       (4 → 5 → 7 → 4)
5	Move to 7	                 4	       (5 → 7 → 5)
6	Move to 5	                 7	       (5 → 5)
7	Only one remains	     Survivor = 5	


Final Output
Eliminating: 3
Eliminating: 6
Eliminating: 2
Eliminating: 1
Eliminating: 4
Eliminating: 7
The survivor is at position: 5


Summary
Circular Linked List Implementation

Each node stores a person's position.

The last node points back to the first node.

Operations Implemented

append(data) → Adds people to the circular linked list.

josephus(k) → Simulates the elimination process and finds the survivor.
'''