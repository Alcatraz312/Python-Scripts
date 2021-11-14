import pandas as pd 

#using dictionary
data1 = {"Rno" : [1,2,3] , "Name" : ["abc","pqr","xyz"] , "Score1":[80,90,100], "Score2":[98,90,100]}

Student1 = pd.DataFrame(data1)
print(Student1)

#add new record 
Student1.loc[3] = [4 , "Manish" , 99 ,100]
print(Student1)

#add new column
Student1["Total"] = Student1["Score1"] + Student1["Score2"]
print(Student1)

#add new column but same value 
Student1["City"] = "Jaipur"
print(Student1)

#add new column but different values 
Student1["City"] = ["Jaipur", "Ajmer", "Jodhpur","Jaipr"]
print(Student1)

#add new column without values
Student1["State"] = pd.NA
print(Student1)

# add or remove more than one column using single statement - Restructure or rearrange dataframe 
Student1 = Student1.reindex(columns = ["Rno","Name","City","State","Score1","Score2"])
print(Student1)

# display multiple records using slicing
print(Student1[0:2])   # does not include final value just like iloc

#using loc 
print(Student1.loc[0:2])

print(Student1.loc[2])    #only shows the given index

#using iloc 
print(Student1.iloc[1])

print(Student1.iloc[0:2])  #won't include the last index 

#to show from top
print(Student1.head(3))

#to show from bottom
print(Student1.tail(2))

# display records based on a condition
print(Student1.loc[Student1["Rno"] == 1])

# display records based on 2 or more conditions
print(Student1.loc[(Student1["Rno"] == 1) | (Student1["Rno"] == 2)])

#display columns 
print(Student1["Rno"])
print(Student1[["Rno","State"]])   #for multiple columns , use 2 square brackets

#display value of just 1 cell 
print(Student1.loc[1 , "City"])

# drop/delete/remove row(s)

Student1 = Student1.drop([0,1])      # here comma is used for range
print(Student1)

# drop/delete/remove column(s)
Student1 = Student1.drop("Rno" , axis = 1)

#Sort index/label or value
print(Student1.sort_index(axis = 0))      #ascending true is default set 
print(Student1.sort_index(ascending = False , axis = 0))
print(Student1.sort_values("Name" , ascending = False))
print(Student1.sort_values(["Score1","Score2"] , ascending = False))



