from collections import deque

# Binary Tree Node
class newNode:
    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def bottomView(root):
    if not root:
        return
    q = [(root, 0)]
    final_hash = {}
    left_most = 0
    final_hash[0] = root.data
    
    while q:
        temp_node, dist_value = q.pop(0)
        final_hash[dist_value] = temp_node.data
        left_most = min(left_most, dist_value)
        if temp_node.left:
            q.append((temp_node.left, dist_value - 1))
    
        if temp_node.right:
            q.append((temp_node.right, dist_value + 1))
    
    final_arr = []
    for idx in range(left_most, len(final_hash)):
        if idx in final_hash:
            final_arr.append(final_hash[idx])
    
    return final_arr

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
    print(bottomView(root))
