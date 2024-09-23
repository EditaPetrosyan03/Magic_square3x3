# Swapping elements in the given array
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Find all permutations 
def find_permutations(arr, result, idx = 0):
    
    if idx == len(arr):
        result.append(arr[:])
        return
    
    for i in range(idx, len(arr)):
        swap(arr, idx, i)
        find_permutations(arr, result, idx + 1,)
        swap(arr, idx, i)

# Create an array, find permutations, and add it to the array
def permute(arr):
    res = []
    find_permutations(arr, res, 0)
    return res

# Check if the permutation that will be a 3x3 matrix is a magic square
def is_magic_square(permutation):
    if sum(permutation[0:3]) == sum(permutation[3:6]) == sum(permutation[6:9]) == sum(permutation[0::3]) == sum(permutation[1::3]) == sum(permutation[2::3]) == sum(permutation[0::4]) == \
    sum(permutation[2:7:2]):
        return True
    else:
        return False

# Creating a magic square
def create_magic_square(permutations):
    magic_square_3x3 = []
    for permutation in permutations:
        if is_magic_square(permutation):
            magic_square_3x3.append([permutation[0:3], permutation[3:6], permutation[6:9]])
    return magic_square_3x3

permutations_list = permute(list(range(1,10)))
magic_square = create_magic_square(permutations_list)
print(magic_square)
