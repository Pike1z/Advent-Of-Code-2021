# Advent of Code 2021 Day 5

BOARD_DIMENSION = 1000 # 999x999 board
heat_map = [0] * BOARD_DIMENSION * BOARD_DIMENSION

# Line class
class Line:
    # Initialize class
    def __init__(self, x1, y1, x2, y2):
        self.p1 = (x1, y1)
        self.p2 = (x2, y2)
    
    # Returns True if line is horizontal
    def ishor(self):
        return self.p1[1] == self.p2[1]
    
    # Returns True if line is vertical
    def isver(self):
        return self.p1[0] == self.p2[0]
    
    # Manhatten distance for x-axis
    def manx(self):
        length = self.p2[0] - self.p1[0]
        if length > 0:
            length += 1
        elif length < 0:
            length -= 1
        return length
    
    # Manhatten distance for y-axis
    def many(self):
        length = self.p2[1] - self.p1[1]
        if length > 0:
            length += 1
        elif length < 0:
            length -= 1
        return length
    
    # Gets direction of diagonal line
    def get_diag_increments(self):
        dx = 1 if self.p2[0] > self.p1[0] else -1
        dy = 1 if self.p2[1] > self.p1[1] else -1

        return dx,dy
    
    # Pretty print format
    def __repr__(self):
        return f'{self.p1} -> {self.p2}'

# Put the line on the heat map
def map_line(line: Line):
    # Get starting points
    x,y = line.p1

    if line.ishor():
        # If line is horizontal find its horizontal length
        length = line.manx()
        # Increment all positions that the line is on
        for i in range(abs(length)):
            heat_map[y * BOARD_DIMENSION + x] += 1
            x += 1 if length > 0 else -1
    elif line.isver():
        # If line is vertical find its vertical length
        length = line.many()
        # Increment all positions that the line is on
        for i in range(abs(length)):
            heat_map[y * BOARD_DIMENSION + x] += 1
            y += 1 if length > 0 else -1
    else:
        ##### PART 2 #####
        # For part 1 just comment this part out
        ##################

        # Doesn't matter if we get x or y length
        length = line.manx()
        # Get diagonal increments
        dx, dy = line.get_diag_increments()
        for i in range(abs(length)):
            heat_map[y * BOARD_DIMENSION + x] += 1
            x += dx
            y += dy

def get_twos():
    return sum(p > 1 for p in heat_map)

lines = []
# Get and parse puzzle input
with open('Inputs/Day5.txt') as f:
    for line in f:
        # Replace -> with a comma
        line = line.strip().replace(' -> ', ',')
        # Split line by commas and convert to integers
        numbers = [int(n) for n in line.split(',')]
        # Add line object to lines list
        lines.append(Line(numbers[0], numbers[1], numbers[2], numbers[3]))

# For each line, map its points
for line in lines:
    map_line(line)

print(f'There are {get_twos()} points on the map where at least 2 lines overlap')