# Definition for Employee.
class Employee:

  def __init__(self, id: int, importance: int, subordinates: List[int]):
    self.id = id
    self.importance = importance
    self.subordinates = subordinates


class Solution:

  def getImportance(self, employees: List['Employee'], id: int) -> int:
    """
        Calculates the total importance of an employee and all their subordinates.

        Args:
            employees: List of Employee objects containing information about each employee.
            id: ID of the employee whose importance is to be calculated.

        Returns:
            Total importance of the specified employee and their subordinates.
        """

    # Helper function to recursively calculate importance
    def get_importance(employee_id):
      total_importance = employee_dict[employee_id].importance
      # Recursively calculate importance of subordinates
      for subordinate_id in employee_dict[employee_id].subordinates:
        total_importance += get_importance(subordinate_id)
      
      return total_importance

    employee_dict = {}

    # Create a dictionary to map employee IDs to their objects
    for emp in employees:
        employee_dict[emp.id] = emp
    return get_importance(id)

    # Get the importance of the specified employee
    return get_importance(id)


if __name__ == "__main__":
  employees = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]
  solution = Solution()
  print(solution.getImportance(employees, 1))  # Output: 11
