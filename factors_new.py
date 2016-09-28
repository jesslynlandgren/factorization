import math

num = int(raw_input('Enter an integer number: '))
factors = [0]

sqrt = int(math.ceil(math.sqrt(num)))

for i in range(1,sqrt):
    if num % i == 0:
        factors.append(i)
        factors.append(num/i)

print sorted(factors)
