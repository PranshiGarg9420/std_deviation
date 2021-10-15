import csv 
import math

with open('standard_deviation.csv',newline='') as f:
    reader= csv.reader(f)
    converted_list = list(reader)

data = converted_list[0]

def mean(data):
    n= len(data)
    total=0
    for i in data:
        total += int(i)
    mean= total/n
    return mean

squared_list=[]
for x in data:
    a=int(x) - mean(data)
    a= a**2
    squared_list.append(a)

sum =0
for x in squared_list:
    sum += x

final = sum/(len(data)-1)

std_dev= math.sqrt(final)
print(std_dev)