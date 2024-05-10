# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: Recursive Sort < O(n^2)
#
# NAME:         Giovanni Rosati
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write a less than O(n^2) sort function `recursive_sort`
# that takes an unordered array of numbers as a parameter
# and returns a sorted array using merge sort or quick
# sort using recursion, rather than loops.
def recursive_sort(array):
    # quick sort
    if len(array) < 2:  # arrays of length < 2 are already sorted
        return array
    pivot = array[0]    # choose initial pivot point
    lower_area = [i for i in array[1:] if i <= pivot]   # items <= value at pivot
    higher_area = [i for i in array[1:] if i > pivot]   # items > value at pivot

    # recursive call to sort smaller and smaller arrays
    return recursive_sort(lower_area) + [pivot] + recursive_sort(higher_area)


def main():
    arrays = [[45, 67, -2, 33, 0, -44, 134, -67], \
              [i for i in range(10)], \
              [i for i in range(10, -1, -1)]]

    for a in arrays:
        print("Unordered:", a)
        print("Sorted:   ", recursive_sort(a))


main()
