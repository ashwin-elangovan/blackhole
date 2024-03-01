# You are given a list of songs where the ith song has a duration of time[i] seconds.

# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

# Example 1:

# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

def numPairsDivisibleBy60(time):
        c = [0] * 60 # Set all values as 0
        res = 0
        for t in time:
            # t=40
            # t%60 = 40
            # -t%60 = 20
            res += c[-t % 60] # Here -t % 60 is basically x % 60
            c[t % 60] += 1
        return res

# time = [30,30,30,30]

# Ideal case t+x = 60
# x = 60-t
# x % 60 = (60 - t) % 60
# Since, t can be greater than 60, we are doing a % 60 to ensure t is always less than 60
# x % 60 = (60 - (t % 60) % 60

