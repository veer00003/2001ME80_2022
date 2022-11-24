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

  # finding rank

	rank1 = []
	for j in range(0, n+2):
		Octant_name_ID_mapping = {'1': "Internal outward interaction", '-1': "External outward interaction", '2': "External Ejection",
								  '-2': "Internal Ejection", '3': "External inward interaction", '-3': "Internal inward interaction", '4': "Internal sweep", '-4': "External sweep"}

		Octant_count = []

		for i in ['1', '-1', '2', '-2', '3', '-3', '4', '-4']:
			Octant_count.append(df.at[j, i])
		Octant_count.sort(reverse=True)  # sorting overall count

		for i in ['1', '-1', '2', '-2', '3', '-3', '4', '-4']:
			for x in range(0, 8):
				if (Octant_count[x] == df.at[j, i]):
					# acessing indices after sorting for ranking
					df.at[j, "Rank("+i+")"] = x+1

		for k in ['1', '-1', '2', '-2', '3', '-3', '4', '-4']:
			if (df.loc[j, "Rank("+str(k)+")"] == 1):
				# Creating Rank1 Octant ID and Rank1 Octant name
				df.at[j, "Rank1 Octant ID"] = k
				df.at[j, "Rank1 Octant Name"] = Octant_name_ID_mapping[str(k)]
				if j == 0:
					continue
				else:
					# appending the rank 1 mod count for mod values
					rank1.append(int(k))

	df.at[n+5, '1'] = 'Octant Id'
	df.at[n+5, '-1'] = 'Octant Name'
	df.at[n+5, '2'] = 'Count of Rank 1 Mod Values'
	for j, x in enumerate([1, -1, 2, -2, 3, -3, 4, -4]):
		df.at[n+6+j, '1'] = x
		df.at[n+6+j, '-1'] = Octant_name_ID_mapping[str(x)]
		# printing the count of octant which is ranked 1
		df.at[n+6+j, '2'] = rank1.count(x)
	df = pd.concat([df.columns.to_frame().T, df], ignore_index=True)
