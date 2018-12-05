

# Read the input and then format it as a list of strings.
with open('../Inputs/input2.txt', 'r') as fp:
    input = fp.read()
input = input.split('\n')
input = input[:-1]          #remove the empty string at the end of the list.


def frequencies(input, val):
    #for given input dictionary of string value, do any have a value == val?
    # input dict = {'a':1, 'b':0} etc.
    #return 1 if true, 0 if false

    for k in input:
        if (input[k] == val):
            return 1
    return 0

def checksums(input):
    # multiple number of strings with exactly two of any letter with number of strings with exactly three of any letter.
    # A string can count for both two and three of a letter, but only once for each.

    two = 0
    three = 0

    for i in range(len(input)):
        # split the string into a list of letters, then sort them
        string = input[i]

        #create a dict with totals for each character.
        totals = {}
        for j in range(len(string)):
            try:
                totals[string[j]] += 1
            except:
                totals[string[j]] = 1

        two += frequencies(totals, 2)
        three += frequencies(totals, 3)

    return two * three

def similarID(input):
    #takes the list of strings.
    strs = []
    for i in range(len(input)):
        j = i
        while j < len(input) - 1:
            j += 1
            diffcount = 0
            for crawl in range(len(input[0])):
                if input[i][crawl] != input[j][crawl]:
                    diffcount += 1
            if diffcount == 1:
                strs.append(input[i])
                strs.append(input[j])
                return strs

def identical(input):
    #takes the list of two strings only.
    # Delete the first character which doesn't match between strings.
    # Return the complete string answer.
    strs = input
    #convert strings to lists
    for i in range(len(strs)):
        strs[i] = list(strs[i])


    for i in range(len(input[0])):
        if input[0][i] != input[1][i]:
            del(input[0][i])
            return ''.join(input[0])


# print(checksums(input))

identical_strings = similarID(input)
print(identical(identical_strings))

# you can compare the strings visually to split out the non-identical letter.