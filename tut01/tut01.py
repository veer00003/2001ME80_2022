#imported pandas library for accessing the input file 
#then used shape to fetch the dimensions of pandas type object
import pandas as pd
df = pd.read_csv(r"C:\Users\hp\OneDrive\Documents\python\2001ME80_2022\tut01\octant_input.csv")
x = df.shape[0]