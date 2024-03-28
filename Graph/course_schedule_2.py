class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
      # Create a dictionary to store prerequisites for each course
      prereq = {idx: [] for idx in range(numCourses)}

      # Populate the prerequisite dictionary
      for crs, req in prerequisites:
          prereq[crs].append(req)

      # Initialize an empty list to store the output order
      output = []
      # Initialize sets to keep track of visited courses and courses in the current DFS path
      visited = set()
      cycle = set()

      # Depth-first search (DFS) function to traverse the course prerequisites
      def dfs(num):
          # If the course has been visited, return True (no need to explore further)
          if num in visited:
              return True
          # If the course is in the current DFS path, there is a cycle, return False
          if num in cycle:
              return False

          # Add the course to the current DFS path
          cycle.add(num)
          # Recursively explore prerequisites of the current course
          for req in prereq[num]:
              if not dfs(req):
                  return False
          # Remove the course from the current DFS path and mark it as visited
          cycle.remove(num)
          visited.add(num)
          # Append the course to the output list (since set does not maintain order)
          output.append(num)
          return True

      # Perform DFS for each course to handle disconnected graphs
      for num in range(numCourses):
          if not dfs(num):
              return []  # If cycle is found, return an empty list
      return output  # Return the topological order of courses
