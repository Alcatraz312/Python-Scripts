import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1 = pd.DataFrame([1,2,4,5,6,7,8])
df2 = pd.DataFrame([3,4,4,3,2,5,6])
data1 = {"Rno" : [1,2,3] , "Name" : ["abc","pqr","xyz"] , "Score1":[80,90,100], "Score2":[98,90,100]}

Student1 = pd.DataFrame(data1)
print(df1.add(df2))

df1.add(df2) # means df1 + df2
df1.radd(df2) # means df2 + df1
df1.sub(df2) # means df1 - df2
df1.rsub(df2) # means df2 - df1
df1.mul(df2) # means df1 * df2
df1.div(df2) # means df1 / df2

print(Student1["Score1"].idxmax())     #to find index with maximum value
print(Student1["Score1"].idxmin())   #to find index with lowest value

data = {'Rno':[1,2,3,4,5], 'Name':['Ankita','Aakash','Aashna','Akshara','Amit'],
'Address':['Jaipur', np.NaN, np.NaN, np.NaN, 'Jaipur']}
df = pd.DataFrame(data)
print(df)

print(df.isnull())    #finds null values as True
print(df.notnull())    #finds null values as false

#to drop colums and rows with null values
print(df.dropna())

#to drop the columns with null values only 
print(df.dropna(axis = 1))

#to replace Na with someting else 
print(df.fillna("No value"))

#flexible comparisons 
print(df[df['Rno']>2])
print(df[df['Rno']<2])
print(df[df['Rno']!= 2])
print(df[df['Rno'] == 2])
print(df[df['Rno']<=2])
print(df[df['Rno']>=2])








