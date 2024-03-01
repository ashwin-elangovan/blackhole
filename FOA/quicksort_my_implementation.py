def quicksort(arr):
  if len(arr) <= 1:
    return arr

  pivot = arr[0]

  left = []
  right = []

  for value in arr[1:]:
    if value <= pivot:
      left.append(value)
    else:
      right.append(value)

  return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([8, 7, 6, 5, 4, 3, 2, 1]))
