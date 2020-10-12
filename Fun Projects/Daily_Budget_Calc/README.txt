(04/24/2020)

A calculator for determining how much a person can spend per day in a month, assuming that they get paid on the first, and still come in over budget.

It functions by determining what the current date is, calculates how many days remain in the current month, and takes an imput (balance) which it divides by remaining days.

Further it generates three plots. A bar chart of how money accumulates over the days to the end of the month, a line plot tracking how the per day budget
changes over the data points, and a line plot of how balance changes.

it then saves the date, daily budget, and imput to a csv file.

BUG:
excel will change the format of the date column into a timestamp, which occasionally causes the date column to have issues with trying to graph.

FIXED by moving away from pickle
On initial run, program will exit due to there not being any pickle data to load into it. TThis can be overcome by commenting out that block of code, and initializing
	mem_dict as an empty dictionary. After that, uncommenting it out will result in the program functioning like it is supposed to.

NOTES:

(04/12/2020) pickle memory storage works like it supposed to besides the one quirk of initialization.

TO DO:

Integrate more of the set up into the function. Currently just doing the final calculation of input/days remaining.

Vizualizations:
	line plot - delta in daily budget day to day

Modeling prediction of coming in over/under budget
	
