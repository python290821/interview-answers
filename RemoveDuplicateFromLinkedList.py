# Define our data structure, each node represent an item in the linked list, each node has it's own value and next node
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value}, {self.next})"


def remove_duplicates(node):
    # Define the current pointer
    curr = node

    # Run while curr and curr.next are not null
    while curr and curr.next:
        # If the value of this node and the next one are the same
        if curr.value == curr.next.value:
            # Assign the next node after the next node instead of the next node (We are skipping this duplicate node)
            curr.next = curr.next.next
        # If the value of this node and the next one are not the same
        else:
            # Set the curr pointer to the next node
            curr = curr.next


node = Node(1, Node(2, Node(2, Node(3, Node(3)))))
remove_duplicates(node)
print(node)
# (1, (2, (3, None)))
