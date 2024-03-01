# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# Example 1:

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Example 2:

# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3

class Solution:
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
      # Get the number of cities (length of isConnected matrix)
      cities_len = len(isConnected)

      # Create a set to keep track of visited cities
      seen = set()

      # Define a depth-first search (DFS) function to explore connected cities
      def dfs(p):
          for idx, value in enumerate(isConnected[p]):
              # If there's a connection to city 'idx' and it hasn't been visited,
              if value == 1 and idx not in seen:
                  seen.add(idx)  # Mark 'idx' as visited
                  dfs(idx)        # Recursively explore connected cities

      # Initialize the count of provinces
      province_count = 0

      # Iterate through all cities to find provinces
      for i in range(cities_len):
          if i not in seen:
              dfs(i)              # Start DFS from unvisited city 'i'
              province_count += 1  # Increment the count for each new province found

      return province_count  # Return the total number of provinces
