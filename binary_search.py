# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Recursive Binary Search
#
# NAME:         Giovanni Rosati
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write a recursive function `search` that
# takes an ordered array of numbers as a parameter
# and a number to search for and returns the index
# of the number in the array using binary, or -1 otherwise. For
# full credit, the search should be implemented using
# recursion, rather than a loop.
def binary_search(array, num):
    return search(array, num, 0, len(array) - 1)

def search(array, num, min, max):
    mid = min + (max - min) //2
    if min > max:
        return -1
    elif num < array[mid]:
        return search(array, num, min, mid-1)
    elif num > array[mid]:
        return search(array, num, mid+1, max)
    else:
        # check if there is an earlier occurance of the same value
        return step_back(array, num, mid)
        return mid
def step_back(array, num, index):
    if array[index-1] != num:
        return index
    else:
        return step_back(array, num, index-1)
def main():
    a = [i for i in range(-1, 10, 2)]
    print(a)
    for n in [1, 0, -1, 2, -2, 4, 5, 6, 7, -67, 134]:
        print("%5d index? %d" % (n, binary_search(a, n)) )

main()
