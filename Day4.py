# Advent of Code 2021 Day 4

BOARD_DIMENSIONS = 5 # 5x5 boards

# Bingo board
class Bingo:
    def __init__(self, values):
        '''
        Bingo Class
        -----------
        Parameters:
            values: list[int]
                list of board values
        '''
        self.complete = False
        self.values = values
        self.checks = [False] * BOARD_DIMENSIONS * BOARD_DIMENSIONS
    
    # Sets self.complete to True if board is complete
    def check_complete(self):
        # Check as long as board is not already complete
        if not self.complete:
            # Check horizontal
            for i in range(BOARD_DIMENSIONS):
                # Assume row is complete
                row_integrity = True
                for j in range(BOARD_DIMENSIONS):
                    # If any element is not checked off, row is incomplete
                    if not self.checks[BOARD_DIMENSIONS * i + j]:
                        row_integrity = False
                    
                # If row is still holding integrity, the board is complete
                if row_integrity:
                    self.complete = True
            
            # Check vertical
            for i in range(BOARD_DIMENSIONS):
                # Assume column is complete
                col_integrity = True
                for j in range(BOARD_DIMENSIONS):
                    if not self.checks[BOARD_DIMENSIONS * j + i]:
                        col_integrity = False
                
                # If col is still holding integrity, the board is complete
                if col_integrity:
                    self.complete = True
    
    # Checks off spots on board that have the given number
    def add_check(self, number):
        # Match value spots to checks
        for i in range(len(self.checks)):
            if self.values[i] == number:
                self.checks[i] = True
        
        # Check if board is complete
        self.check_complete()
    
    # Gets the sum of all unchecked numbers
    def unchecked_sum(self):
        sum = 0
        for i in range(len(self.checks)):
            if not self.checks[i]:
                sum += self.values[i]
        
        return sum
    
    # Pretty print form of the board
    def __repr__(self):
        repr = '\n'
        for i in range(BOARD_DIMENSIONS):
            row = ''
            for j in range(BOARD_DIMENSIONS):
                if self.checks[BOARD_DIMENSIONS * i + j]:
                    row += ' x '
                else:
                    row += f'{self.values[BOARD_DIMENSIONS * i + j]:2d} '
            repr += row + '\n'
        
        return repr

# Bingo complete
def game_won(boards):
    winner = None
    for board in boards:
        if board.complete:
            winner = board
    
    return winner

# Get formatted puzzle data
random_numbers = []
bingo_boards = []

with open('Inputs/Day4.txt') as f:
    # Get each number as an int from the random number line split by commas
    random_line = f.readline().strip().split(',')
    random_numbers = [int(s) for s in random_line]

    # Read until end of file
    while f.readline():
        # loop condition got rid of blank line
        board_values = []
        # Read through 5 lines and get a list of values
        for i in range(BOARD_DIMENSIONS):
            line_str = f.readline().strip().split()
            line_numbers = [int(s) for s in line_str]
            board_values.extend(line_numbers)
        
        # Add values to bingo boards
        bingo_boards.append(Bingo(board_values))

##### PART 1 #####

# Play Bingo

# Loop until a winner is found or random numbers run out
winner = None
number = 0
while not winner and len(random_numbers) > 0:
    number = random_numbers.pop(0)

    # Check off number on each board
    for board in bingo_boards:
        board.add_check(number)

    winner = game_won(bingo_boards)

winning_value = winner.unchecked_sum() * number
print(f'The final score of the board is {winning_value} points')

##### PART 2 #####

# Continue playing Bingo

# Loop until 1 board remains
bingo_boards.remove(winner)
number = 0
while len(bingo_boards) > 1 and len(random_numbers) > 0:
    number = random_numbers.pop(0)

    # Maintain a list of winners for this number call
    winners = []

    for board in bingo_boards:
        board.add_check(number)
        
        # If that number caused the board to win, track it
        if board.complete:
            winners.append(board)
    
    # Remove winning boards
    for winner in winners:
        bingo_boards.remove(winner)

# Continue with last board until it wins
winner = bingo_boards[0]
while not winner.complete:
    number = random_numbers.pop(0)
    winner.add_check(number)

winning_value = winner.unchecked_sum() * number
print(f'The final score of the last winner is {winning_value} points')