import unittest

#read input, split lines into list items.
with open('../Inputs/input3.txt', 'r') as fp:
    input = fp.read()
input = input.split('\n')   # split each line into a new list item.
input = input[:-1]          # remove trailing ''.

# generate a blank grid of 1000x1000 0s. Each digit represents 1 sq in of cloth.
# We add to them to generate the frequency of claims which use that square of cloth.

def init_square_fabric_array(width):
    #arbitrary width
    fabric = []
    for i in range(0, width):
        fabric.append([])
        for j in range(0, width):
            fabric[i].append(0)
    return fabric

# Input is in format
# `#2 @ 941,233: 16x14`
# Number of claim, starting co-ord (top left), width x height of cloth piece.
# We don't need anything before the coordinates, so let's strip those.


# Iterate the list of inputs, slice it up and output a list of [x coord, y coord, width, height, id] as ints.
def clean_data(input):
    for i in range(len(input)):
        j = input[i]
        j = j.split(' ')[2:]
        coords = j[0].split(',')
        coords[1] = coords[1].replace(':', '')
        dimensions = j[1].split('x')
        id = [input[i].split(' ')[0].replace('#', '')]
        output = coords + dimensions + id
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
        for y in range(claim[1], claim[1] + claim[3]): #y-origin + height:
            for x in range(claim[0], claim[0] + claim[2]): #x-origin + width
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


def find_nonclash_claim(input, fabric):
    #input the marked up fabric, run over the input list again, return the Id of the non-clashing cloth.
    for i in range(len(input)):
        claim = input[i]
        id = claim[4]
        unique = True
        for y in range(claim[1], claim[1] + claim[3]): #y-origin + height:
            for x in range(claim[0], claim[0] + claim[2]): #x-origin + width
                if fabric[y][x] > 1:
                    unique = False
        if unique:
            return id


fabric = init_square_fabric_array(1000)
input = clean_data(input)
fabric = mark_fabric(input, fabric)
print(find_num_dupes(fabric))


## Now, find the ID number of the only claim which doesn't overlap.
## I have modified the clean_data method to leave the ID at the end of the list.

print(find_nonclash_claim(input, fabric))


class MyFirstTests(unittest.TestCase):
    def blank_fabric(self):
        input = 10
        expected = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        self.assertEqual(expected, init_square_fabric_array(input))

    def test_input_lists(self):
        input = ["#2 @ 941,233: 16x14"]
        expected = [[941, 233, 16, 14, 2]]
        self.assertEqual(clean_data(input), expected)

    def test_input_lists2(self):
        input = ["#123 @ 3,2: 5x4"]
        expected = [[3, 2, 5, 4, 123]]
        self.assertEqual(clean_data(input), expected)

    def test_fabric_marks2(self):
        input = ["#123 @ 3,2: 5x4"]
        list = clean_data(input)
        fabric = [[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]]
        expected = [[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]]
        self.assertEqual(expected, mark_fabric(list, fabric))

    def test_fabric_marks(self):
        input = [[1,3,4,4], [3,1,4,4], [5,5,2,2]]
        fabric = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        expected = [[0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,0],[0,0,0,1,1,1,1,0],[0,1,1,2,2,1,1,0],[0,1,1,2,2,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0]]
        self.assertEqual(expected, mark_fabric(input, fabric))

    def test_num_dupes(self):
        input = [[0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,0],[0,0,0,1,1,1,1,0],[0,1,1,2,2,1,1,0],[0,1,1,2,2,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0]]
        expected = 4
        self.assertEqual(find_num_dupes(input), expected)
