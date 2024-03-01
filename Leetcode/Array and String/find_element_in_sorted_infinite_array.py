# Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array.
# If the array is infinite, that means we don’t have proper bounds to apply binary search. So in order to find position of key, first we find bounds and then apply binary search algorithm.
# Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with high index element,
# ->if it is greater than high index element then copy high index in low index and double the high index.
# ->if it is smaller, then apply binary search on high and low indices found.


# Define a binary search function that searches for an element 'element' in a sorted array 'arr' between indices 'l' and 'h'.
def binary_search(arr, l, h, element):
  # Check if 'l' is less than or equal to 'h'. If not, return -1 indicating the element is not found.
  if l <= h:
    # Calculate the middle index of the current search range.
    # if we use mid = (low + high)/2 then it might lead to overflow
    mid = l + (h - l) // 2

    # Check if the middle element is equal to the target 'element'.
    if arr[mid] == element:
      return mid
    # If the middle element is less than 'element', search in the right half of the array.
    elif arr[mid] < element:
      return binary_search(arr, mid + 1, h, element)
    # Otherwise, search in the left half of the array.
    return binary_search(arr, l, mid - 1, element)

  # If 'l' is greater than 'h', return -1 indicating the element is not found.
  return -1


# Define a function to find the position of an element in a sorted array with exponential search.
def findPos(arr, element):
  l, h = 0, 1

  # Double the value of 'h' while it's less than 'element'.
  while arr[h] < element:
    l = h
    h = 2 * h

  # Call the binary search function to search for 'element' in the range [l, h].
  return binary_search(arr, l, h, element)


# Driver function
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
element_to_be_found = 10

# Call the 'findPos' function to find the position of 'element_to_be_found' in 'arr'.
ans = findPos(arr, element_to_be_found)

# Check if the result is -1, indicating that the element was not found, and print the appropriate message.
if ans == -1:
  print("Element not found")
# Otherwise, print the index where the element was found.
else:
  print("Element found at index", ans)
