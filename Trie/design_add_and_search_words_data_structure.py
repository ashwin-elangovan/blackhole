class TrieNode:

  def __init__(self):
    self.children = {}  # Dictionary to store child nodes
    self.end_of_word = False  # Flag to mark the end of a word


class WordDictionary:

  def __init__(self):
    self.root = TrieNode()  # Initialize the root node of the trie

  def addWord(self, word: str) -> None:
    current = self.root
    # Traverse through each character in the word
    for char in word:
      # If the character is not present in the current node's children, add it
      if char not in current.children:
        current.children[char] = TrieNode()
      # Move to the next node
      current = current.children[char]
    # Mark the end of the word
    current.end_of_word = True

  def search(self, word: str) -> bool:
    self.res = None  # Variable to store the search result
    self.dfs(self.root, word)  # Start depth-first search from the root
    return self.res

  def dfs(self, root, word):
    # Base case: If the word is empty
    if not word:
      # Check if the current node marks the end of a word
      if root.end_of_word:
        self.res = True  # Set the search result to True
      return

    # If the first character of the word is a wildcard '.'
    if word[0] == '.':
      # Iterate through each child node of the current node
      for key, value in root.children.items():
        if self.res:  # If the word is found, terminate DFS
          return
        # Recursively search for the remaining part of the word
        self.dfs(root.children[key], word[1:])
    else:
      # If the first character of the word is a specific character
      if word[0] in root.children:
        # Move to the child node corresponding to the character
        child = root.children[word[0]]
        # Recursively search for the remaining part of the word
        self.dfs(child, word[1:])
      # If the character is not present in the current node's children, return
      else:
        return


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
