import functions as f
this_many = 100

'''
----- goal -----
compare the number of comparisons for the various sorting algorithms

----- instructions -----
print the number of comparisons for each algorithm
for example, your output might look like this:

calling sorting algorithms with 100 items...
bubble count:  4950
insertion count:  2359
merge count:  544
quicksort count:  639
'''

# TODO #1 write the 'reset_list' function (in functions.py)
# TODO #2 write the 'swap' function (in functions.py)
# TODO #3 test your code so far (the merge and quick sorts at the bottom should work)

# TODO #4
# TODO call the reset_list function
# TODO call the bubble_sort function
# TODO print the 'counter' variable



# TODO #5
# TODO call the reset_list function
# TODO call the insertion_sort function
# TODO print the 'counter' variable





# ------------------------------------------------
# these two algorithms have been completed for you
# notice how to call the functions and how to get the counter variable
lst = f.reset_list(this_many)
lst = f.merge_sort(lst)
print("merge count: ", f.counter)

lst = f.reset_list(this_many)
lst = f.quicksort(lst)
print("quicksort count: ", f.counter)



# optional ------------------------------------------------
# use matplotlib to make your graph!
# pseudocode:
# make a list of lengths that you want to include
# make lists for each sort algorithm that will store the a list of 'counter' values
# iterate through this list
# reset the list, call the sort algorithm, append the 'counter' value to this algorithms list
# reset the list, call the next sort algorithm, append the 'counter' value to this algorithms list
# when the loop is finished, graph your data!