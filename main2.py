class Node:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def sorted_arr_to_bst(arr):
  if not arr:
    return None

  mid = (len(arr)) // 2
  root = Node(arr[mid])

  root.left = sorted_arr_to_bst(arr[:mid])
  root.right = sorted_arr_to_bst(arr[mid + 1:])

  return root


def btree_to_sorted_arr(root, nodes):
  if not root:
    return None
  btree_to_sorted_arr(root.left, nodes)
  nodes.append(root.data)
  btree_to_sorted_arr(root.right, nodes)


def preorder(root):
  if root is None:
    return None

  print(root.data)
  preorder(root.left)
  preorder(root.right)


def lca(root, value1, value2):
  if root is None:
    return None
  if value1 < root.data and value2 < root.data:
    lca_val = lca(root.left, value1, value2)
  elif value1 > root.data and value2 > root.data:
    lca_val = lca(root.right, value1, value2)
  else:
    return root
  return lca_val


arr = []


def isBST(root, floor=float('-inf'), ceil=float('inf')):
  if root is None:
    return True
  if not floor < root.data < ceil:
    return False
  return isBST(root.left, floor, root.data) and isBST(root.right, root.data,
                                                      ceil)


def nth_largest(root, c):
  # global c

  if root is None or c[0] >= 2:
    return

  nth_largest(root.right, c)

  c[0] += 1
  if (c[0] == 2):
    print(f"{c[0]}th largest data", root.data)
    return

  nth_largest(root.left, c)


def k_sum(root, cc, ac, sum):
  if root is None or cc[0] >= ac[0]:
    return

  k_sum(root.left, cc, ac, sum)

  cc[0] += 1
  sum[0] += root.data
  if (cc[0] == ac[0]):
    return

  k_sum(root.right, cc, ac, sum)


root = Node(50)
root.left = Node(25)
root.right = Node(75)
root.left.left = Node(24)
root.left.right = Node(26)

# root = Node(10)
# root.left = Node(8)
# root.left.left = Node(7)
# root.left.left.left = Node(6)
# root.left.left.left.left = Node(5)

nodes = []
btree_to_sorted_arr(root, nodes)
print(nodes)
r = sorted_arr_to_bst(nodes)
print("Root", r.data)
print("RL", r.left.data)
print("RL", r.left.left.data)
print("RR", r.right.data)
print("RL", r.right.left.data)
preorder(r)

check = lca(root, 24, 26)
print(check.data)

print(isBST(root))
# print(checkBST())
c = [0]
print(nth_largest(root, c))

cc = [0]
ac = [3]
sum = [0]
k_sum(root, cc, ac, sum)
print(sum)
