from collections import Counter
from typing import List


class Solution:

  def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    # Approach 1: Using Counter and While Loop

    # Count the occurrences of each type of student's preference
    students_ctr = Counter(students)

    # Initialize the counter for students who have eaten their sandwiches
    students_who_ate = 0

    # Get the total number of students
    total_students = len(students)

    # Iterate until all students have eaten their sandwiches or there are no more sandwiches left
    while students_who_ate < total_students and students_ctr[
        sandwiches[students_who_ate]] > 0:
      # Reduce the count of the student's preferred sandwich from the counter
      students_ctr[sandwiches[students_who_ate]] -= 1
      # Increment the count of students who have eaten
      students_who_ate += 1

    # Calculate the number of students who couldn't eat their sandwiches
    remaining_students = total_students - students_who_ate
    return remaining_students

    # Approach 2: Using Counter and For Loop

    # Count the occurrences of each type of student's preference
    students_ctr = Counter(students)

    # Initialize the total number of students
    students_len = len(students)

    # Iterate through each sandwich in the list
    for s in sandwiches:
      # If there are still students who prefer the current sandwich
      if students_ctr[s] > 0:
        # Decrement the count of students who prefer the current sandwich
        students_ctr[s] -= 1
        # Decrement the total number of students
        students_len -= 1
      else:
        # If no students prefer the current sandwich, break the loop
        break

    # Return the number of students who couldn't eat their sandwiches
    return students_len
