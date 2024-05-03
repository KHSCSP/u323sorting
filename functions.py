import random
counter = 0

# TODO this function will return a list with random items
def reset_list(this_many):
    global counter
    counter = 0
    # to be 'fair', we'll create the same randomized list each time
    random.seed(42) # <- you can change that if you want
    # TODO create a list with 'this_many' random items
    # TODO return that list
    pass


# TODO this function swaps two items in a list
def swap(lst, i, j):
    # TODO write the swap algorithm
    pass


# TODO bubble sort
def bubble(lst):
    global counter
    # TODO write the bubble sort algorithm
    # note: this function does not need to return anything
    pass



# TODO insertion sort
def insertion(lst):
    global counter
    # TODO write the insertion sort algorithm
    # note: this function does not need to return anything
    pass








# ------------------------------------------------
# these two algorithms have been completed for you
# ----- merge sort -----
# source: pltw.org
def merge_sort(arr):
    """ Merge Sort, Complexity: O(n log(n)) """
    
    # our recursive base case
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    
    # perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # merge each side together
    return merge(left, right, arr.copy())



def merge(left, right, merged):
    """ Merge helper, Complexity: O(n) """
    global counter
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        counter += 1 # add to the comparison counter
        # sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    # add the left overs if there's any left to the result
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    # add the left overs if there's any left to the result
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    # return result
    return merged



# ----- quick sort ----
# source: pltw.org
def partition(array, start, end):
    global counter
    """ quicksort partitioning, using end """
    pivot = array[end]
    L = start
    R = end
    while L < R:
        while array[L] < pivot:
            L += 1
            counter += 1
        while array[R] > pivot:
            R -= 1
            counter += 1
        swap(array, L, R)
        # avoid hanging on the same numbers
        if ( array[L] == array[R] ):
            L += 1
    return R


def _quicksort(array, start, end):
    """ Recursive quicksort function """
    global counter
    if start < end:
        counter += 1
        split = partition(array, start, end)
        _quicksort(array, start, split-1)
        _quicksort(array, split+1, end)


def quicksort(array):
    _quicksort(array, 0, len(array)-1)
