n = 10000
h = {}
for i in range(1,n+1):
    sod = sum_of_digits(i)
    if sod not in h:
        h[sod] = 1 
    else:
        h[sod]+=1

def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum+= number % 10
        number //= 10
    return sum

max_value = max(h.values())
print(max_value)
max_keys = [key for key, value in h.items() if value == max_value]
print(len(max_keys))