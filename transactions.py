logs = [["supply", "item", "2", "100"], ["supply", "item2", "3", "60"],
        ["sell", "item", "1"], ["sell", "item", "1"], ["sell", "item2", "2"],
        ["return", "item2", "1", "60", "40"], ["sell", "item2", "1"],
        ["sell", "item2", "1"]]

sell_logs = []
supply_logs = {}

for log in logs:
  operation, item, count = log[0], log[1], log[2]
  if operation == "supply":
    if item not in supply_logs:
      supply_logs[item] = []
    for i in range(int(count)):
      supply_logs[item].append(int(log[3]))
  elif operation == "sell":
    nums = int(count)
    sell_value = 0
    for i in range(nums):
      sell_value += int(supply_logs[item].pop(0))
    sell_logs.append(sell_value)
    sell_value = 0
  elif operation == "return":
    for i in range(int(count)):
      supply_logs[item].insert(0, int(log[4]))

print(sell_logs)
