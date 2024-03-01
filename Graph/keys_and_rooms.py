# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

# Example 1:

# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation: 
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.

# Example 2:

# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

# Trick: The visits are not sequential

def canVisitAllRooms(self, rooms: List[List[int]) -> bool:
  # Get the total number of rooms
  len_rooms = len(rooms)
  # Create a list to track whether each room has been visited
  visited = [False] * len_rooms
  # Mark the first room (room 0) as visited since we start from there
  visited[0] = True
  # Create a stack to perform depth-first search starting from room 0
  stack = [0]

  # Continue searching until the stack is empty
  while stack:
      # Get the current room from the stack
      current_room = stack.pop()
      # Iterate through the keys in the current room
      for key in rooms[current_room]:
          # If the connected room has not been visited, mark it as visited
          if not visited[key]:
              visited[key] = True
              # Add the connected room to the stack for further exploration

  # Check if all rooms have been visited by checking if all elements in 'visited' are True
  return all(visited)
