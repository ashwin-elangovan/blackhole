# Python3 program to construct binary
# tree from given array in level
# order fashion Tree Node

# Helper function that allocates a
# new node
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# Function to insert nodes in level order
def insertLevelOrder(arr, idx, length):
    root = None

    # Check if the current index is within the bounds of the array
    if idx < length:
        # Create a new node with the data at the current index
        root = newNode(arr[idx])

        # Recursively insert the left child by doubling the current index and adding 1
        root.left = insertLevelOrder(arr, 2 * idx + 1, length)

        # Recursively insert the right child by doubling the current index and adding 2
        root.right = insertLevelOrder(arr, 2 * idx + 2, length)

    # Return the root node of the constructed binary tree
    return root

# Function to print tree nodes in
# InOrder fashion
def inOrder(root):
    if root != None:
        # Traverse the left subtree
        inOrder(root.left)

        # Print the data of the current node
        print(root.data, end=" ")

        # Traverse the right subtree
        inOrder(root.right)

# Driver Code
if __name__ == '__main__':
    # Input array to construct the binary tree
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    length = len(arr)

    # Construct the binary tree from the input array
    root = insertLevelOrder(arr, 0, length)

    # Print the nodes of the binary tree in InOrder fashion
    inOrder(root)
