#imported pandas library for accessing the input file 
#then used shape to fetch the dimensions of pandas type object
import pandas as pd
df = pd.read_excel(r"C:\Users\hp\OneDrive\Documents\python\2001ME80_2022\tut02\input_octant_transition_identify.xlsx")
x = df.shape[0]



#here used the mean() function for finding the average of U
U_avg = df['U'].mean()
#similarly here used mean function for V and W
V_avg = df['V'].mean()
W_avg = df['W'].mean()

#made a column to store average of U
df['U Avg']=U_avg
#and here given only 1st place of line to U avg otherwise average value will print in whole column
df['U Avg']=df['U Avg'].head(1)

#similarly here made column for average of V and W
#also here given only 1st place of line to W and V average otherwise average value will print in whole column
df['V Avg']=V_avg
df['V Avg']=df['V Avg'].head(1)

df['W Avg']=V_avg
df['W Avg']=df['W Avg'].head(1)



#here defined the X,Y,Z and X=U' , Y=V' , Z=W'
X = df['U'] - U_avg
Y = df['V'] - V_avg
Z = df['W'] - W_avg

#here made the column for storing X and named the column as U'=U - U_avg and similarly done for Y and Z.
df["U'=U - U_avg"] = X
df["V'=V - V_avg"] = Y
df["W'=W - W_avg"] = Z


#here made the column for storing the value of octant
df.insert(10, column="Octant", value="")
# Octant=[]
#using loop for taking the all values of the row and column
for i in range(0,x):
#for ease defined M, N, O
    M= df["U'=U - U_avg"][i]
    N= df["V'=V - V_avg"][i]
    O= df["W'=W - W_avg"][i]
    
#finding octant value by using conditional statements if and elif

#1st quadrant(1) and positive z(+)
    if M>0 and N>0 and O>0:
        print(1)
        df["Octant"][i] = 1
        
#1st quadrant(1) and negative z(-)
    elif M>0 and N>0 and O<0:
        print(-1)
        df["Octant"][i] =-1
        
#2nd quadrant(2) and positive z(+)
    elif M<0 and N>0 and O>0:
        print(2)
        df["Octant"][i] =2
        
#2nd quadrant(2) and negative z(-)
    elif M<0 and N>0 and O<0:
        print(-2)
        df["Octant"][i] =-2
        
#3rd quadrant(3) and positive z(+)
    elif M<0 and N<0 and O>0:
        print(3)
        df["Octant"][i] =3
        
#3rd quadrant(3) and negative z(-)
    elif M<0 and N<0 and O<0:
        print(-3)
        df["Octant"][i] =-3
        
#4th quadrant(4) and positive z(+)
    elif M>0 and N<0 and O>0:
        print(4)
        df["Octant"][i] =4
        
#4th quadrant(4) and negative z(-)
    elif M>0 and N<0 and O<0:
        print(-4)
        df["Octant"][i] =-4