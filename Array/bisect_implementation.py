import bisect

def bisect_left(a, x, lo=0, hi=None):
  while lo < hi:
    mid = (lo + hi) // 2
    if a[mid] < x:
      lo = mid + 1
    else:
      hi = mid
  return lo

def bisect_right(a, x, lo=0, hi=None):
  while lo < hi:
    mid = (lo + hi) // 2
    if a[mid] <= x:
      lo = mid + 1
    else:
      hi = mid
  return lo


arr = [1, 5, 6, 8, 9]

print(bisect_left(arr, 5, 0, 4))
print(bisect_right(arr, 5, 0, 4))
