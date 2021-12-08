# Advent of Code 2021 Day 3

# Bit tracking class
class BitTracker:
    def __init__(self):
        self.ones = 0
        self.zeros = 0
    
    def increment(self, bit):
        if bit == '1':
            self.ones += 1
        else:
            self.zeros += 1
    
    def getmax(self):
        return '1' if self.ones >= self.zeros else '0'
    
    def getmin(self):
        return '1' if self.ones < self.zeros else '0'
    
    def __repr__(self):
        return f'(1: {self.ones}|0: {self.zeros})'

# Get puzzle input
bit_codes = []
with open('Inputs/Day3.txt') as f:
    for line in f:
        bit_codes.append(line.strip())

bit_tracks = [BitTracker() for i in range(len(bit_codes[0]))]

# Run through bit codes
for bit_code in bit_codes:
    for i in range(len(bit_code)):
        bit_tracks[i].increment(bit_code[i])

gamma_rate = ''
epsilon_rate = ''

# From most common bits form gamma and epsilon rates
for bit_track in bit_tracks:
    gamma_rate += bit_track.getmax()
    epsilon_rate += bit_track.getmin()

# Converts binary represented string into decimal number
gamma_rate_dec = int(gamma_rate, 2)
epsilon_rate_dec = int(epsilon_rate, 2)

print(gamma_rate_dec * epsilon_rate_dec)

##### PART 2 #####

def get_most_common_bit(i, binaries):
    most_common = BitTracker()
    for bin in binaries:
        most_common.increment(bin[i])
    
    return most_common

# Scrub for oxygens
oxygen_list = bit_codes.copy()
# Go over each most common bit
i = 0
while len(oxygen_list) > 1 and i < len(bit_tracks):
    most_common = get_most_common_bit(i, oxygen_list)
    oxygen_list = list(filter(lambda o: o[i] == most_common.getmax(), oxygen_list))
    i += 1

# Scrub for co2
co2_list = bit_codes.copy()
i = 0
# Go over each most common bit
while len(co2_list) > 1 and i < len(bit_tracks):
    most_common = get_most_common_bit(i, co2_list)
    co2_list = list(filter(lambda o: o[i] == most_common.getmin(), co2_list))
    i += 1

oxygen_rating = int(oxygen_list[0], 2)
co2_rating = int(co2_list[0], 2)

print(f'Life support rating: {oxygen_rating * co2_rating}')