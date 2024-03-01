# You are given an array of numbers, with each being a 0 or 1. All 1 s are arranged at the beginning of the array and 0 s at the end. 

# Get the number of seconds.


import collections

zerostoone = 2
arr = [1,1,1,0,0,0]
counts = collections.Counter(arr)
zerocount = counts[0]
onecount = counts[1]
seconds = 0
while(True):
    if zerocount >= zerostoone:
        arr = arr[: len(arr) - zerostoone]
        arr = [1] + arr
        zerocount = zerocount - zerostoone
        onecount = onecount + 1
        seconds += 1
    elif onecount > 0:
        arr.pop(0)
        arr.append(0)
        zerocount += 1
        onecount -= 1
        seconds += 1
    else:
        break

print(seconds)