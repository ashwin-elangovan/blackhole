from collections import deque

# Binary Tree Node
class newNode:
    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printRightView(root):
    if not root:
        return
    res = []
    q = deque([root])
  
    while q:
        size = len(q)
  
        for i in range(size, 0, -1):
            current_node = q.popleft()
  
            # Print the rightmost element at the level
            if i == 1:
                res.append(current_node.data)
  
            # Add left and right nodes to the queue if they exist
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
    return res



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
    print(printRightView(root))
