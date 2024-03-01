# word = "dwcblqnxtrwtqmtqenidhxnifdbmdvobwmcvwjxgbyjzgvrqzlskjbfirauguhyyjhlotuckssrkqzppzbqd"

# word_len = len(word)
# print(word_len)
# for w_idx in range(0, word_len // 2):
#   if word[w_idx] != word[-(w_idx + 1)]:
#     print(word[w_idx], word[-(w_idx + 1)])
#     break
#   if w_idx == (word_len // 2 - 1):
#     print(word)

# def threeSum(nums):
#   nums.sort()
#   final_arr = []
#   final_idx = len(nums) - 1

#   for idx, value in enumerate(nums):
#     left, right = idx + 1, final_idx
#     target = 0 - value

#     while left < right:
#       if nums[left] + nums[right] == target:
#         final_arr.append([value, nums[left], nums[right]])
#       elif nums[left] + nums[right] < target:
#         left += 1
#       else:
#         right -= 1
#   return final_arr

# nums = [-1, 0, 1, 2, -1, -4]
# print(threeSum(nums))

from collections import defaultdict


class Graph:

  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self, key, value):
    self.graph[key].append(value)

  def dfsUtil(self, v, visited):

    visited.add(v)

    print(v, end=' ')

    for neighbour in self.graph[v]:
      if neighbour not in visited:
        self.dfsUtil(neighbour, visited)

  def dfs(self, v):
    visited = set()
    self.dfsUtil(v, visited)


# Driver's code
if __name__ == "__main__":
  g = Graph()
  g.addEdge(0, 1)
  g.addEdge(0, 2)
  g.addEdge(1, 2)
  g.addEdge(2, 0)
  g.addEdge(2, 3)
  g.addEdge(3, 3)

  print("Following is Depth First Traversal (starting from vertex 2)")

  # Function call
  g.dfs(2)
