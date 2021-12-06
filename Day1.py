# Advent of Code 2021 Day 1

# Get puzzle input
depths = []
with open('Inputs/Day1.txt') as f:
    for line in f.readlines():
        depths.append(int(line.strip()))

##### PART 1 #####

# Count depth increases
last_depth = depths[0]
increases = 0
for i in range(1, len(depths)):
    if (depths[i] > last_depth):
        increases +=1 
    last_depth = depths[i]

print('Total number of increases:', increases)

##### PART 2 #####
def list_sum(my_list):
    sum = 0

    for num in my_list:
        sum += num
    
    return sum

last_sum = list_sum(depths[0:3])
increases = 0
for i in range(3, len(depths)):
    curr_sum = list_sum(depths[i-2:i+1])
    if (curr_sum > last_sum):
        increases += 1
    last_sum = curr_sum

print('Total number of increases:', increases)