# Gas station problem

# Brute force

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

n = len(gas)

for i in range(0, n):
    total_cost = 0
    j = i
    stop_count = 0
    # Stop count must become equal to n
    while stop_count < n:
        total_cost += gas[j%n] - cost[j%n] # To go to 0th index after last index
        if total_cost < 0:
            break
        stop_count += 1
        j += 1
    if total_cost >= 0 and stop_count == n:
        print(i)


#########

# O(N) Solution


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

n = len(gas)
start = 0
total_surplus = 0

for i in range(n):
    total_surplus += gas[i] - cost[i]
    surplus += gas[i] - cost[i]
    if surplus < 0:
        surplus = 0
        start = i + 1

print(-1 if total_surplus < 0 else start)
        


