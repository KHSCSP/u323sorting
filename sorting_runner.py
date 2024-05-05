import functions as f
how_many = 100

'''
----- goal -----
analyze the efficiency for the various sorting algorithms

----- instructions -----
print the number of comparisons for each algorithm
for example, your output might look like this:

calling sorting algorithms with 100 items...
bubble count:  4xxx
insertion count:  2xxx
merge count:  5xx
quicksort count:  6xx
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
print("\nresetting list...sorting with merge...")
lst = f.reset_list(how_many)
lst = f.merge_sort(lst)
merge_ans = f.counter
print("merge count: ", merge_ans)


print("\nresetting list...sorting with quick...")
lst = f.reset_list(how_many)
lst = f.quicksort(lst)
quick_ans = f.counter
print("quicksort count: ", quick_ans)





# making a bar graph ------------------------------
import matplotlib.pyplot as plt
# TODO make a list of the names of the algorithms
# TODO make a list of the 'answers' from the algorithms
# TODO make a barchart: plt.bar(algs_list, nums_list)


