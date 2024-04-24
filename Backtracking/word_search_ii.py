class TrieNode():
  def __init__(self):
      self.children = {}  # Dictionary to store child nodes
      self.isWord = False  # Flag to indicate if the node represents the end of a word

  def add_word(self, word):
      current = self
      # Traverse the trie to add the word character by character
      for ch in word:
          if ch not in current.children:
              current.children[ch] = TrieNode()  # Create a new node if the character doesn't exist
          current = current.children[ch]  # Move to the next node
      current.isWord = True  # Mark the last node as the end of a word

class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
      self.root = TrieNode()  # Create the root node of the trie
      # Add all the words in the list to the trie
      for word in words:
          self.root.add_word(word)

      visited, result = set(), set()  # Initialize sets to track visited cells and found words

      def dfs(row, col, node, current_word):
          # Base cases to terminate recursion
          if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in visited or board[row][col] not in node.children:
              return False

          visited.add((row, col))  # Mark the cell as visited
          current_word += board[row][col]  # Add the character to the current word
          node = node.children[board[row][col]]  # Move to the corresponding node in the trie

          if node.isWord:
              result.add(current_word)  # Add the word to the result if it's found in the trie

          # Recursive DFS calls in four directions
          dfs(row-1, col, node, current_word)  # Up
          dfs(row, col-1, node, current_word)  # Left
          dfs(row+1, col, node, current_word)  # Down
          dfs(row, col+1, node, current_word)  # Right

          visited.remove((row, col))  # Backtrack: Remove the cell from visited set

      # Iterate through each cell on the board and start DFS from there
      for row in range(len(board)):
          for col in range(len(board[0])):
              dfs(row, col, self.root, "")  # Start DFS from the current cell with an empty current word

      return result  # Return the set of found words
