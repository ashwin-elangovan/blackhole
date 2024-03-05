# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to find height of tree using BFS
def height_by_bfs(root):
    # Base Case
    if root is None:
        return 0

    q = []
    q.append(root)
    height = 0

    # Loop while queue is not empty
    while q:
        # nodeCount (queue size) indicates number of nodes at current level
        nodeCount = len(q)

        # Dequeue all nodes of current level and Enqueue all nodes of next level
        while nodeCount > 0:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodeCount -= 1
        # Add one to height as we are going to next level
        height += 1

    return height

# Function to find height of tree using DFS recursion
def height_by_dfs(root):
    if root is None:
        return 0

    lheight = height_by_dfs(root.left)
    rheight = height_by_dfs(root.right)

    if lheight > rheight:
        return lheight + 1
    else: # This handles the case for leaf node where lheight and rheight will be 0
        return rheight + 1

# Example usage:
if __name__ == "__main__":
    # Constructing a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Calculate height using DFS recursion
    print("Height of the binary tree:", height_by_dfs(root))