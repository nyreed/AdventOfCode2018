with open('Inputs/input1.txt', 'r') as fp:
    nums = fp.read()
nums = nums.split('\n')
nums = nums[:-1]

for i in range(len(nums)): #convert input data to list of ints
    nums[i] = int(nums[i])

def frequency(nums):
    num_iterations = 0
    total = 0
    results = {}
    while True:
        num_iterations += 1
        print("iteration %i" % num_iterations)
        print("number of results %i" % (len(results)))
        for i in range(len(nums)):
            total += nums[i]
            # if the total isn't already in the dictionary, an error is raised and the
            # except path runs, adding the total to the dict. This is much faster than
            # Storing the results in a list and checking each result [if total in results:].
            try:
                results.pop(total)
                return total
            except:
                results[total] = 1



print(sum(nums)) #this is the sum of all the numbers. Challenge 1.

print(frequency(nums)) # Find the first total which is reached twice.

