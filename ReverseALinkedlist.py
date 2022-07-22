# Define our data structure, each node represent an item in the linked list, each node has it's own value and next node
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = str(self.val)
        if self.next:
            res += str(self.next)
        return res


class Solution(object):
    def reverse(self, node):
        # Define a current variable that is a pointer to the node
        curr = node
        # Define a prev variable that currently points to None
        prev = None

        # while the current is not none
        while curr is not None:
            # Declare temporary variable that is pointing to the next node
            tmp = curr.next
            # Change the next node to point to the prev
            curr.next = prev
            # Set the prev node to point to the current node
            prev = curr
            # Set the current node to point to the temp
            curr = tmp

        return prev


node = Node(1, Node(2, Node(3, Node(4, Node(5)))))

print(Solution().reverse(node))
# 54321
