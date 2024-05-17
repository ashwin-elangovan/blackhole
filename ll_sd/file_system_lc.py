class TrieNode:
    def __init__(self, val):
        self.children = {}  # Dictionary to store child nodes
        self.val = val  # Value associated with the node

class FileSystem:
    def __init__(self):
        self.root = TrieNode(0)  # Initialize the root of the file system with value 0

    def createPath(self, path: str, value: int) -> bool:
        # Method to create a new path with the given value
        names = path[1:].split('/')  # Split the path into directory names
        curr = self.root  # Start traversal from the root node
        for i, name in enumerate(names):
            if i == len(names) - 1:  # If it's the last directory name
                if name in curr.children:  # If the directory already exists
                    return False  # Return False as path already exists
                curr.children[name] = TrieNode(value)  # Create a new node for the directory with the given value
                return True  # Return True indicating successful creation of the path
            if name not in curr.children:  # If parent path doesn't exist
                return False  # Return False as parent path doesn't exist
            curr = curr.children[name]  # Move to the next directory node

    def get(self, path: str) -> int:
        # Method to get the value associated with the given path
        curr = self.root  # Start traversal from the root node
        names = path[1:].split('/')  # Split the path into directory names
        for i, name in enumerate(names):
            if name not in curr.children:  # If directory doesn't exist
                return -1  # Return -1 indicating path not found
            curr = curr.children[name]  # Move to the next directory node
        return curr.val  # Return the value associated with the last directory in the path
