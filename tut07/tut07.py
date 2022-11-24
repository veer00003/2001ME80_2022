from datetime import datetime
start_time = datetime.now()

import math
# imported pandas library for accessing the input file
# then used shape to fetch the dimensions of pandas type object
import pandas as pd



def octant_analysis(mod, df):
	# AVERAGE

	# here used the mean() function for finding the average of U
	U_avg = df['U'].mean()
	# similarly here used mean function for V and W
	V_avg = df['V'].mean()
	W_avg = df['W'].mean()

	# made a column to store average of U
	df['U Avg'] = U_avg
	# and here given only 1st place of line to U avg otherwise average value will print in whole column
	df['U Avg'] = df['U Avg'].head(1)

	# similarly here made column for average of V and W
	# also here given only 1st place of line to W and V average otherwise average value will print in whole column
	df['V Avg'] = V_avg
	df['V Avg'] = df['V Avg'].head(1)

	df['W Avg'] = V_avg
	df['W Avg'] = df['W Avg'].head(1)

	# here defined the X,Y,Z and X=U' , Y=V' , Z=W'
	X = df['U'] - U_avg
	Y = df['V'] - V_avg
	Z = df['W'] - W_avg

	# here made the column for storing X and named the column as U'=U - U_avg and similarly done for Y and Z.
	df["U'=U - U_avg"] = X
	df["V'=V - V_avg"] = Y
	df["W'=W - W_avg"] = Z

	# FINDING OCTANT

	# here made the column for storing the value of octant
	df.insert(10, column="Octant", value="")
	# Octant=[]
	# using loop for taking the all values of the row and column
	for i in range(0, x):
		# for ease defined M, N, O
		M = df["U'=U - U_avg"][i]
		N = df["V'=V - V_avg"][i]
		O = df["W'=W - W_avg"][i]

	# finding octant value by using conditional statements if and elif

	# 1st quadrant(1) and positive z(+)
		if M > 0 and N > 0 and O > 0:
			print(1)
			df["Octant"][i] = 1

	# 1st quadrant(1) and negative z(-)
		elif M > 0 and N > 0 and O < 0:
			print(-1)
			df["Octant"][i] = -1

	# 2nd quadrant(2) and positive z(+)
		elif M < 0 and N > 0 and O > 0:
			print(2)
			df["Octant"][i] = 2

	# 2nd quadrant(2) and negative z(-)
		elif M < 0 and N > 0 and O < 0:
			print(-2)
			df["Octant"][i] = -2

	# 3rd quadrant(3) and positive z(+)
		elif M < 0 and N < 0 and O > 0:
			print(3)
			df["Octant"][i] = 3

	# 3rd quadrant(3) and negative z(-)
		elif M < 0 and N < 0 and O < 0:
			print(-3)
			df["Octant"][i] = -3

	# 4th quadrant(4) and positive z(+)
		elif M > 0 and N < 0 and O > 0:
			print(4)
			df["Octant"][i] = 4

	# 4th quadrant(4) and negative z(-)
		elif M > 0 and N < 0 and O < 0:
			print(-4)
			df["Octant"][i] = -4

			# COUNTING OCTANT

	# user input
	df.at[1, ''] = 'User Input'
	# creating row
	df.at[0, 'Octant ID'] = 'Overall Count'

	# counting the 1 and -1 putting list of Octant ID
	df.at[0, '1'] = list(df['Octant']).count(1)
	df.at[0, '-1'] = list(df['Octant']).count(-1)

	# counting the 1 and -1 putting list of Octant ID
	df.at[0, '2'] = list(df['Octant']).count(2)
	df.at[0, '-2'] = list(df['Octant']).count(-2)

	# counting the 1 and -1 putting list of Octant ID
	df.at[0, '3'] = list(df['Octant']).count(3)
	df.at[0, '-3'] = list(df['Octant']).count(-3)

	# counting the 1 and -1 putting list of Octant ID
	df.at[0, '4'] = list(df['Octant']).count(4)
	df.at[0, '-4'] = list(df['Octant']).count(-4)

	# COUNTING OCTANT VALUES FOR RANGES AND PROCESSING FOR FINAL SOLUTION

	# defining boundry for ranges
	boundary = []

	mod = 5000
	n = math.ceil(len(df.index)/mod)
	df.at[1, 'Octant ID'] = 'Mod {}'.format(mod)

	# using loop to devide all value of data in 6 ranges of 5000 difference
	for i in range(math.ceil(len(df.index)/mod)):
		boundary.append(i*mod)
	# appending the boundry and for last value taking the index length of df
	boundary.append(len(df.index))

	# countig the octants value in each range division by using loop
	for i in range(len(boundary) - 1):
		df.at[2 + i, 'Octant ID'] = str(boundary[i]) + \
			" to " + str(boundary[i + 1] - 1)

		df.at[2 + i, '1'] = df['Octant'].iloc[boundary[i]
			:(boundary[i+1])].value_counts()[1]
		df.at[2 + i, '-1'] = df['Octant'].iloc[boundary[i]
			:(boundary[i+1])].value_counts()[-1]

		df.at[2 + i, '2'] = df['Octant'].iloc[boundary[i]
			:(boundary[i+1])].value_counts()[2]
		df.at[2 + i, '-2'] = df['Octant'].iloc[boundary[i]
			:(boundary[i+1])].value_counts()[-2]

		df.at[2 + i, '3'] = df['Octant'].iloc[boundary[i]
			:(boundary[i+1])].value_counts()[3]
		df.at[2 + i, '-3'] = df['Octant'].iloc[boundary[i]
			:(boundary[i+1])].value_counts()[-3]

		df.at[2 + i, '4'] = df['Octant'].iloc[boundary[i]
			:(boundary[i+1])].value_counts()[4]
		df.at[2 + i, '-4'] = df['Octant'].iloc[boundary[i]
			:(boundary[i+1])].value_counts()[-4]
