from typing import List
from collections import defaultdict, deque
from itertools import groupby


class Solution:

  def findAllPeople(self, n: int, meetings: List[List[int]],
                    firstPerson: int) -> List[int]:
    # Initialize the set 'can' with 0 and the first person
    can = {0, firstPerson}

    # Group meetings by their third element (time) and iterate over the groups
    for _, grp in groupby(sorted(meetings, key=lambda x: x[2]),
                          key=lambda x: x[2]):
      # Initialize a set 'queue' to store people who need to be processed
      queue = set()
      # Initialize a defaultdict 'graph' to store the graph representation of the meetings
      graph = defaultdict(list)

      # Iterate over the meetings in the current time group
      for x, y, _ in grp:
        # Add edges between people who attended the same meeting
        graph[x].append(y)
        graph[y].append(x)
        # Add people to the queue who have attended meetings
        if x in can: queue.add(x)
        if y in can: queue.add(y)

      # Convert the set 'queue' to a deque for efficient popping
      queue = deque(queue)

      # Perform BFS traversal starting from people in the 'queue'
      while queue:
        # Remove a person from the left end of the 'queue'
        x = queue.popleft()
        # Explore the neighbors of the current person
        for y in graph[x]:
          # If the neighbor is not already included in 'can'
          if y not in can:
            # Add the neighbor to 'can' and enqueue it for further exploration
            can.add(y)
            queue.append(y)

    # Return the set 'can' containing all the people reachable from the initial set
    return can
