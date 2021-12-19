# Advent of Code 2021 Day 6

# Get puzzle input
school = []
with open('Inputs/Day6.txt') as f:
    input = f.readline()
    days = input.strip().split(',')
    school = [int(day) for day in days]

# Simulate the growth of the fish
def simulate_growth(SIM_DAYS, school):
    school_size = len(school)
    # Use a weekly cycle to add new fish to the school size
    week = [0] * 7
    # Array to compensate for newborn fish having to wait longer
    new_borns = [0] * 7
    for fish in school:
        week[fish] += 1

    # O(n) runtime compared to longer algorithms I tried before
    for i in range(SIM_DAYS):
        school_size += week[i % 7]
        new_borns[(i + 2) % 7] += week[i % 7]
        week[i % 7] += new_borns[i % 7]
        new_borns[i % 7] = 0

    print(f'After {SIM_DAYS} days there are {school_size} fish')

##### PART 1 #####
simulate_growth(80, school)
##### PART 2 #####
simulate_growth(256, school)