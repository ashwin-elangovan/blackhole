class Solution:
  def uniquePathsIII(self, grid: List[List[int]]) -> int:
      # Get the number of rows and columns in the grid
      row_len = len(grid)
      col_len = len(grid[0])

      # Initialize the count of paths to 0
      self.paths_count = 0

      # Initialize the count of cells (including the initial cell) to 1
      cells_count = 1 

      # Initialize variables to store the starting row and column indices
      row_idx, col_idx = 0, 0

      # Initialize a set to keep track of visited cells
      visited = set()

      # Depth-first search (DFS) function to explore paths in the grid
      def dfs(row, col, count):
          # Base case: If the current cell is out of bounds or an obstacle (-1), return
          if row < 0 or col < 0 or row >= row_len or col >= col_len or grid[row][col] == -1:
              return

          # Base case: If the current cell has been visited before, return
          if (row, col) in visited:
              return

          # Base case: If the current cell is the end cell (2)
          if grid[row][col] == 2:
              # If all non-obstacle cells have been visited (count matches the total cells count), increment paths_count
              if count == cells_count:
                  self.paths_count += 1
              return

          # Mark the current cell as visited
          visited.add((row, col))

          # Explore adjacent cells in all four directions
          dfs(row+1, col, count+1)  # Down
          dfs(row-1, col, count+1)  # Up
          dfs(row, col+1, count+1)  # Right
          dfs(row, col-1, count+1)  # Left

          # Backtrack: Unmark the current cell as visited
          visited.remove((row, col))

      # Iterate through each cell in the grid to find the starting cell (1) and count the total cells
      for row in range(row_len):
          for col in range(col_len):
              if grid[row][col] == 0:  # Empty cell
                  cells_count += 1
              elif grid[row][col] == 1:  # Starting cell
                  row_idx = row
                  col_idx = col

      # Start DFS from the starting cell
      dfs(row_idx, col_idx, 0)

      # Return the total count of unique paths
      return self.paths_count
