class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
      # Set to store visited coordinates during DFS
      visited = set()

      # Define DFS function
      def dfs(x, y, str_len):
          # If the current position matches the word's length, we found the word
          if str_len == len(word):
              return True

          # Boundary conditions and checking if cell is already visited or doesn't match the word
          if x >= len(board) or y >= len(board[0]) or x < 0 or y < 0:
              return False
          
          if (x, y) in visited or board[x][y] != word[str_len]:
              return False

          # Mark the cell as visited
          visited.add((x, y))

          # Explore adjacent cells in all four directions
          # If any of the recursive calls returns True, then return True
          self.res = dfs(x + 1, y, str_len + 1) or dfs(x, y + 1, str_len + 1) or dfs(x, y - 1, str_len + 1) or dfs(x - 1, y, str_len + 1)

          # Remove the cell from visited set after exploration
          visited.remove((x, y))

          # Return the result of DFS
          return self.res

      # Iterate through each cell on the board
      for x in range(len(board)):
          for y in range(len(board[0])):
              # If the starting letter matches the first letter of the word, start DFS
              if board[x][y] == word[0]:
                  if dfs(x, y, 0):
                      return True
      # If the word is not found after exploring all cells, return False
      return False
