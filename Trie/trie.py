class TrieNode:

  def __init__(self):
    """
      Trie node class to represent each node in the trie.
      """
    self.children = {}  # Dictionary to store child nodes
    self.endOfWord = False  # Flag to indicate if the node represents the end of a word


class Trie:

  def __init__(self):
    """
      Initializes the Trie data structure with an empty root node.
      """
    self.root = TrieNode()  # Create the root node of the Trie

  def insert(self, word: str) -> None:
    """
      Inserts a word into the Trie.

      Args:
          word: The word to be inserted into the Trie.
      """
    cur = self.root  # Start traversal from the root node

    # Traverse each character of the word
    for char in word:
      # If the current character is not in the children of the current node, add it
      if char not in cur.children:
        cur.children[char] = TrieNode()
      # Move to the next node
      cur = cur.children[char]

    cur.endOfWord = True  # Mark the end of the word

  def search(self, word: str) -> bool:
    """
      Searches for a word in the Trie.

      Args:
          word: The word to search for in the Trie.

      Returns:
          True if the word is found in the Trie, False otherwise.
      """
    cur = self.root  # Start traversal from the root node

    # Traverse each character of the word
    for char in word:
      # If the current character is not in the children of the current node, the word is not present
      if char not in cur.children:
        return False
      # Move to the next node
      cur = cur.children[char]

    return cur.endOfWord  # Check if the last node represents the end of a word

  def startsWith(self, prefix: str) -> bool:
    """
      Determines if there is any word in the Trie that starts with the given prefix.

      Args:
          prefix: The prefix to search for in the Trie.

      Returns:
          True if there exists any word in the Trie that starts with the given prefix, False otherwise.
      """
    cur = self.root  # Start traversal from the root node

    # Traverse each character of the prefix
    for char in prefix:
      # If the current character is not in the children of the current node, no word starts with the prefix
      if char not in cur.children:
        return False
      # Move to the next node
      cur = cur.children[char]

    return True  # Prefix found in the Trie


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
