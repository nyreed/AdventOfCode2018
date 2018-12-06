import unittest

#read input, split lines into list items.
with open('../Inputs/input3.txt', 'r') as fp:
    input = fp.read()
input = input.split('\n')   # split each line into a new list item.
input = input[:-1]          # remove trailing ''.

# generate a blank grid of 1000x1000 0s. Each digit represents 1 sq in of cloth.
# We add to them to generate the frequency of claims which use that square of cloth.

def init_fabric_array():
    #arbitrary width
    fabric = []
    zeros = []
    for i in range(0, 1500):
        zeros.append(0)
    for i in range(0, 1500):
        fabric.append(zeros)
    return fabric

# Input is in format
# `#2 @ 941,233: 16x14`
# Number of claim, starting co-ord (top left), width x height of cloth piece.
# We don't need anything before the coordinates, so let's strip those.


# Iterate the list of inputs, slice it up and output a list of [x coord, y coord, width, height] as ints.
def clean_data(input):
    for i in range(len(input)):
        j = input[i]
        j = j.split(' ')[2:]
        coords = j[0].split(',')
        coords[1] = coords[1].replace(':', '')
        dimensions = j[1].split('x')
        output = coords + dimensions
        for k in range(len(output)):
            output[k] = int(output[k])
        input[i] = output
    return input

#Increment the value at each co-ord for each time it's needed for a fabric claim.
#Input as list of claims in list format -> [x, y, width, height]
def mark_fabric(input, fabric):
    fabric = fabric
    for i in range(len(input)):
        claim = input[i]
        for y in range(claim[1], claim[1] + claim[3] + 1): #y-origin + height:
            for x in range(claim[0], claim[0] + claim[2] + 1): #x-origin + width
                fabric[y][x] += 1
    return fabric

def find_num_dupes(fabric):
    #iterate over whole matrix, return number of squares value > 1
    dupes = 0
    for y in range(len(fabric)):
        for x in range(len(fabric[y])):
            if fabric[y][x] > 1:
                dupes += 1
    return dupes

fabric = init_fabric_array()
input = clean_data(input)
fabric = mark_fabric(input, fabric)
print(find_num_dupes(fabric))



class MyFirstTests(unittest.TestCase):
    def test_input_lists(self):
        input = ["#2 @ 941,233: 16x14"]
        expected = [[941, 233, 16, 14]]
        self.assertEqual(clean_data(input), expected)
    def test_fabric_marks(self):
        input = [[1,3,4,4], [3,1,4,4], [5,5,2,2]]
        fabric = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        expected = [[0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,0],[0,0,0,1,1,1,1,0],[0,1,1,2,2,1,1,0],[0,1,1,2,2,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0]]
        self.assertEqual(mark_fabric(input, fabric), expected)
    def test_num_dupes(self):
        input = [[0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,0],[0,0,0,1,1,1,1,0],[0,1,1,2,2,1,1,0],[0,1,1,2,2,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0]]
        expected = 4
        self.assertEqual(find_num_dupes(input), expected)
