# Advent of Code 2021 Day 8

SEG_NUMS = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}

# Display class
class Display:
    def __init__(self, line):
        parts = line.split('|')
        self.sig_patterns = parts[0].strip().split(' ')
        self.outputs = parts[1].strip().split(' ')
        self.map = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None}
    
    def getlength(self, length):
        segment = ''
        for pattern in self.sig_patterns:
            if len(pattern) == length:
                segment = pattern
        
        return segment
    
    def getone(self):
        return self.getlength(2)
    
    def getseven(self):
        return self.getlength(3)
    
    def getfour(self):
        return self.getlength(4)
    
    def geteight(self):
        return self.getlength(7)
    
    def getsixes(self):
        sixes = []
        for pattern in self.sig_patterns:
            if len(pattern) == 6:
                sixes.append(pattern)
        
        return sixes
    
    def getfives(self):
        fives = []
        for pattern in self.sig_patterns:
            if len(pattern) == 5:
                fives.append(pattern)
        
        return fives
    
    # Maps randomized signal patterns to expected seven segment display
    def getmap(self):
        # Map a
        one = self.getone()
        seven = self.getseven()
        unique_to_seven = ''
        for char in seven:
            if char not in one:
                unique_to_seven = char
        self.map[unique_to_seven] = 'a'
        a = unique_to_seven

        # Get b and d specifics
        four = self.getfour()
        unique_to_four = []
        for char in four:
            if char not in one:
                unique_to_four.append(char)
        
        # Get e and g specifics
        eight = self.geteight()
        unique_to_eight = []
        for char in eight:
            if char not in four and char != unique_to_seven:
                unique_to_eight.append(char)
        
        # Get all horizontal segments
        fives = self.getfives()
        horizontal = []
        for char in fives[0]:
            if char in fives[1] and char in fives[2] and char != unique_to_seven:
                horizontal.append(char)
        
        # Map d and g
        d = ''
        g = ''
        for horiz in horizontal:
            if horiz in unique_to_four:
                self.map[horiz] = 'd'
                d = horiz
            else:
                self.map[horiz] = 'g'
                g = horiz
        
        # Map b and e
        unique_to_four.remove(d) # b
        unique_to_eight.remove(g) # e
        self.map[unique_to_four[0]] = 'b'
        b = unique_to_four[0]
        self.map[unique_to_eight[0]] = 'e'

        # Get f
        sixes = self.getsixes()
        unique_to_sixes = [] # All sixes share a,b,g,f
        for char in sixes[0]:
            if char in sixes[1] and char in sixes[2]:
                unique_to_sixes.append(char)
        
        # Filter out a,b,g
        unique_to_sixes.remove(a)
        unique_to_sixes.remove(b)
        unique_to_sixes.remove(g)

        # Map f
        self.map[unique_to_sixes[0]] = 'f'
        f = unique_to_sixes[0]

        # Map c
        self.map[one.replace(f, '')] = 'c'

    # Given an output segment, get what number it should represent
    def get_real_num(self, segment):
        mapped_seg = ''
        for char in segment:
            mapped_seg += (self.map[char])
        ordered_seg = ''.join(sorted(mapped_seg))

        return SEG_NUMS[ordered_seg]


entries = []
# Get puzzle input
with open('Inputs/Day8.txt') as f:
    for line in f:
        entries.append(Display(line))

##### PART 1 #####
unique_count = 0
segment_sum = 0
for entry in entries:
    outputs = entry.outputs
    entry.getmap() # Get the map while we're in this loop
    tmp_sum = 0
    for output in outputs:
        tmp_sum *= 10
        tmp_sum += entry.get_real_num(output)
        if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7:
            unique_count += 1
    segment_sum += tmp_sum

print(f'There are {unique_count} instances of 1s, 4s, 7s, and 8s')

##### PART 2 #####
print(f'The sum of decoded values is {segment_sum}')