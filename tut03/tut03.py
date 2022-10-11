#imported pandas library for accessing the input file 
#then used shape to fetch the dimensions of pandas type object
import pandas as pd
df = pd.read_excel(r"C:\Users\hp\OneDrive\Documents\python\2001ME80_2022\tut02\input_octant_transition_identify.xlsx")
x = df.shape[0]
df.head()
