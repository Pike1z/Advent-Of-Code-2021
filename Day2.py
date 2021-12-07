# Advent of Code 2021 Day 2

# Get puzzle input
commands = []
with open('Inputs/Day2.txt') as f:
    for line in f:
        # Get command
        commands.append(line.strip().split(' '))

##### PART 1 #####
# Starting coordinates
x, y = 0, 0

# Follow commands
for command in commands:
    direction = command[0]
    magnitude = int(command[1])
    if direction == 'forward':
        x += magnitude
    elif direction == 'up':
        y -= magnitude
    elif direction == 'down':
        y += magnitude

print(f'Final position calculation: {x * y}')

##### PART 2 #####
aim, x, y = 0, 0, 0

# Follow commands
for command in commands:
    direction = command[0]
    magnitude = int(command[1])
    if direction == 'forward':
        x += magnitude
        y += (magnitude * aim)
    elif direction == 'up':
        aim -= magnitude
    elif direction == 'down':
        aim += magnitude

print(f'Final position calculation: {x * y}')