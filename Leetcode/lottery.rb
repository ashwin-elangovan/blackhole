n = 22
h = {}

def sum_of_digits(number)
    sum = 0
    while number > 0
        sum+= number % 10
        number /= 10
    end
    sum
end 

for i in 1..n
    sod = sum_of_digits(i)
    p sod
    next h[sod] = 1 if h[sod].nil?
    h[sod] += 1
end

max_value = h.values.max

result = h.select { |k,v| v == 3 }.keys.length





