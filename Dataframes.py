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

