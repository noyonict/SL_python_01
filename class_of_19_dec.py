from statistics import mean
from functools import reduce

sample_list = [78, 23, 1, 2, 89, 3, 4, 9, 20, 35]

# Average
sum_ = 0
for i in sample_list:
    sum_ += i

print('Average by loop:', sum_/len(sample_list))

print('Average by mean function:', mean(sample_list))

print('Average by sum function:', sum(sample_list)/len(sample_list))

print('Average by reduce function:', reduce(lambda x, y: x + y, sample_list)/len(sample_list))


#  Above Average
above_average = []
for i in sample_list:
    if i > mean(sample_list):
        above_average.append(i)
print('Above Average Items by loop:', above_average)

print('Above Average Items by list comprehension:', [i for i in sample_list if i > mean(sample_list)])

print('Above Average Items by filter function:', list(filter(lambda x: x > mean(sample_list), sample_list)))


# Multiply by Average Value
mul_list = []
for i in sample_list:
    mul_list.append(i * mean(sample_list))

print('Multiple by Average value by loop:', mul_list)

print('Multiple by Average value by list comprehension:', [i * mean(sample_list) for i in sample_list])

print('Multiple by Average value by map function:', list(map(lambda x: x * mean(sample_list), sample_list)))


# Multiply
mul_ = 1

for i in sample_list:
    mul_ *= i

print('Multiply by loop:', mul_)

print('Multiply by reduce function:', reduce(lambda x, y: x * y, sample_list)/len(sample_list))
