# Add and search words

class TrieNode:
  def __init__(self):
      self.children = {}
      self.end_of_word = False

class WordDictionary:
  def __init__(self):
      self.root = TrieNode()

  def addWord(self, word: str) -> None:
      current = self.root
      for char in word:
          if char not in current.children:
              current.children[char] = TrieNode()
          current = current.children[char] 
      current.end_of_word = True


  def search(self, word: str) -> bool:
      self.res = None
      curr = self.root
      self.dfs(curr, word)
      return self.res

  def dfs(self, curr_node, word):
      if not curr_node:
          return False

      if not word:
          if curr_node.end_of_word:
              self.res = True
          return

      if word[0] == '.':
          for child in curr_node.children:
              if self.res:
                  return
              self.dfs(curr_node.children[child], word[1:])
      else:
          if word[0] not in curr_node.children:
              return
          else:
              self.dfs(curr_node.children[word[0]], word[1:])