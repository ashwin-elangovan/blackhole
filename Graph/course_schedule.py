class Solution:

  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Create a dictionary to store the prerequisites for each course
    course = {}
    for idx in range(numCourses):
      course[idx] = []

    # Populate the dictionary with prerequisites
    for current_course, prereq in prerequisites:
      course[current_course].append(prereq)

    # Set to keep track of courses visited along the current DFS path
    cycle = set()  # To avoid cycles
    visited = set()

    # Depth-first search (DFS) function to detect cycles in the graph
    def dfs(crs):
      # If the current course is already in the cycle set, it means a cycle is detected
      if crs in cycle:
        return False
      # If there are no prerequisites for the current course or it has been visited before, return True
      if course[crs] == [] or crs in visited:
        return True

      # Add the current course to the cycle set to track the DFS path
      cycle.add(crs)

      # Recursively check the prerequisites of the current course
      for req in course[crs]:
        if not dfs(
            req):  # If a cycle is detected in the prerequisites, return False
          return False

      # Remove the current course from the cycle set after checking its prerequisites
      cycle.remove(crs)
      # Mark the current course as visited
      visited.add(crs)
      return True

    # Iterate through each course and run DFS to detect cycles
    for crs in range(numCourses):
      if not dfs(crs):  # If a cycle is detected during DFS, return False
        return False
    # If no cycle is detected in any course, return True
    return True
