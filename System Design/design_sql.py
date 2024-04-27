class SQL:

  def __init__(self, names: List[str], columns: List[int]):
    # Initialize the database dictionary to store tables and their properties
    self.db = {}

    # Iterate over the list of table names and columns
    for idx, table in enumerate(names):
      # Create an empty dictionary to represent each table
      self.db[table] = {}

      # Initialize the current row ID to 0
      self.db[table]["curr_id"] = 0

      # Store the number of columns for each table
      self.db[table]["columns_count"] = columns[idx]

      # Create a dictionary to store the values for each row in the table
      self.db[table]["values"] = {}

  def insertRow(self, name: str, row: List[str]) -> None:
    # Increment the current row ID for the specified table
    table = self.db[name]
    table["curr_id"] += 1

    # Store the values of the new row in the table's values dictionary
    table["values"][table["curr_id"]] = row

  def deleteRow(self, name: str, rowId: int) -> None:
    # Delete the specified row from the table's values dictionary
    del self.db[name]["values"][rowId]

  def selectCell(self, name: str, rowId: int, columnId: int) -> str:
    # Retrieve the value from the specified cell in the table
    # Adjust the columnId by 1 since it is 1-indexed
    return self.db[name]["values"][rowId][columnId - 1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name, row)
# obj.deleteRow(name, rowId)
# param_3 = obj.selectCell(name, rowId, columnId)
