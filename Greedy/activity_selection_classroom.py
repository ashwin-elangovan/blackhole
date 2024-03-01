# You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. 

# Examples:  

# Input: start[]  =  {10, 12, 20}, finish[] =  {20, 25, 30}
# Output: 0 2
# Explanation: A person can perform at most two activities. The 
# maximum set of activities that can be executed 
# is {0, 2} [ These are indexes in start[] and finish[] ]

# Input: start[]  =  {1, 3, 0, 5, 8, 5}, finish[] =  {2, 4, 6, 7, 9, 9};
# Output: 0 1 3 4
# Explanation: A person can perform at most four activities. The 
# maximum set of activities that can be executed 
# is {0, 1, 3, 4} [ These are indexes in start[] and finish[]

# How does Greedy Choice work for Activities sorted according to finish time? 
# Let the given set of activities be S = {1, 2, 3, …n}, and activities are sorted by finish time. The greedy choice is to always pick activity 1. How come activity 1 always provides one of the optimal solutions?

#  We can prove it by showing that if there is another solution B with the first activity other than 1, then there is also a solution A of the same size as activity 1 as the first activity. Let the first activity selected by B be k, then there always exist A = {B – {k}} U {1}.

# Note: The activities in B are independent and k has the smallest finishing time among all. Since k is not 1, finish(k) >= finish(1))

def max_activities(arr, n):
    selected = []

    # The first activity always gets selected
    i = 0
    selected.append(arr[i])

    for j in range(1, n):
        # If this activity has start time greater than or equal to
        # the finish time of previously selected activity, then select it
        if arr[j][0] >= arr[i][1]:
            selected.append(arr[j])
            i = j
    return selected

# Driver code
if __name__ == '__main__':
    start_times = [5, 1, 3, 0, 5, 8]
    finish_times = [9, 2, 3, 4, 6, 7, 9]
    
    # Create a list of activity pairs with finish times and start times
    # sorted by increasing finishing times
    activity = [[x, y] for y, x in sorted(zip(finish_times, start_times))]
    n = len(activity)  # Number of activities

    # Function call to find the maximum activities that can be performed
    selected = max_activities(activity, n)

    print("Following activities are selected:", end="")
    for i in range(len(selected)):
        # Print the selected activities
        print("", selected[i], end=",")



