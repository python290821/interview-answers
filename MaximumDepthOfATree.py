# Note - Recursion won't work on large trees, due to the limit on stack limit size.
# Iteration, on the other hand, uses heap space which is limited only by how
# much memory is in the computer.

# Define Data structure the represents a single node that has value, left node and right node
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, n):
        # Define a list with one tuple inside that will be called stack,
        # the first value of the tuple is the depth, and the second is the node
        stack = [(1, n)]
        # Define max_depth variable that it's value is 0 for now
        max_depth = 0
        # While the length of the stack is greater than zero, that means while there are items in the stack
        while len(stack) > 0:
            # pop the first item from the stack into depth and node variables since the item is a tuple
            depth, node = stack.pop()
            if node:
                # Set the max_depth to the maximum value between previous max_depth and depth that was
                # popped from the stack
                max_depth = max(max_depth, depth)
                # Append both the right and left nodes of the current node with the depth increased by 1
                stack.append((depth + 1, node.left))
                stack.append((depth + 1, node.right))
        return max_depth

    # The recursive solution
    def maxDepthRecursive(self, n):
        if not n:
            return 0
        return max(self.maxDepthRecursive(n.left) + 1,
                   self.maxDepthRecursive(n.right) + 1)


n = Node(1)
n.left = Node(2)
n.right = Node(3)
n.left.left = Node(4)

print(Solution().maxDepth(n))
# 3

print(Solution().maxDepthRecursive(n))
# 3
