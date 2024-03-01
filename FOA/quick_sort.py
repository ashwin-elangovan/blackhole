def partition(arr, low, high):
  i = low - 1
  pivot = arr[high]
  # high is not considered since its the pivot
  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  i += 1
  arr[i], arr[high] = arr[high], arr[i]
  return i


def quicksort(arr, low, high):
  if low < high:
    pivot = partition(arr, low, high)

    quicksort(arr, low, pivot - 1)
    quicksort(arr, pivot + 1, high)


# Example usage:
my_list = [10, 7, 8, 9, 1, 5]
quicksort(my_list, 0, len(my_list) - 1)
print("Sorted list:", my_list)
