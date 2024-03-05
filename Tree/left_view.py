from collections import deque

# Binary Tree Node
class newNode:
    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0

def printLeftView(root):
    if not root:
        return

    q = deque([root])

    while q:
        size = len(q)

        for i in range(size):
            current_node = q.popleft()

            # Print the leftmost element at the level
            if i == 0:
                print(current_node.data, end=" ")

            # Add left and right nodes to the queue if they exist
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)



# Driver Code
if __name__ == "__main__":

    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    printLeftView(root)
