from collections import Counter
 
# initializing lists
test_list1 = [1, 3, 4, 5, 1, 3, 3]
test_list2 = [1, 3, 5]
 
# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))
 
# Using collections.Counter()
# Difference of list including duplicates
res = list((Counter(test_list1) - Counter(test_list2)).elements())

# Using set differences to find the difference of lists without duplicates
res = list(set(test_list1) - set(test_list2))