# Advent of Code 2021 Day 7

# Get puzzle input
crabs = []
with open('Inputs/Day7.txt') as f:
    input = f.readline().strip()
    crabs = [int(c) for c in input.split(',')]

def move_cost(crab, position):
    dist = abs(crab - position)
    cost = dist * (dist + 1) // 2

    return cost

# Get the cost to align crabs to a certain position
def align_cost1(position):
    cost = 0
    for crab in crabs:
        cost += abs(position - crab)
    
    return cost

# Get the cost to align crabs with different fuel usage
def align_cost2(position):
    cost = 0
    for crab in crabs:
        cost += move_cost(crab, position)
    
    return cost

# Get max and min of list
max_pos = max(crabs)
min_pos = min(crabs)
cost1 = align_cost1(min_pos)
cost2 = align_cost2(min_pos)

for i in range(max_pos + 1):
    tmp_cost1 = align_cost1(i)
    tmp_cost2 = align_cost2(i)
    if tmp_cost1 < cost1:
        cost1 = tmp_cost1
    if tmp_cost2 < cost2:
        cost2 = tmp_cost2

print(f'Cheapest cost is {cost1}')
print(f'Part 2 cheapest cost is {cost2}')