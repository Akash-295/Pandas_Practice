
# Student Performance Analyser (Beginner Level Project.)

import pandas as pd

std_data = {
    "Student_ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Name":["Usato", "Iruma", "Kunon", "Ichigo", "Rick", "Giyu", "Polka", "Remuru"],
    "Class": ['A','A','B','A','B','B','C','B'],
    "Maths":[78, 96, 80, 69, 92, 84, 71, 82],
    "Science": [89, 91, 84, 67,None, 95, 86, 90],
    "English": [89, 74, 69, 84, 91, 93, 62, 73]
}

std_df = pd.DataFrame(std_data)

#save the dataframe as csv file 
std_df.to_csv("Student Data.csv")

#loading the dataset
print("Student DataSet: \n",std_df)

#finding the missing values in the dataset 
print("Any Missing Value: \n",std_df.isnull().sum())

#fill marks with subject average 

avg_mark = std_df["Science"].mean()
std_df["Science"] = std_df["Science"].fillna(avg_mark)
print("New Student DataSet: \n", std_df)

#adding new Total Marks column in the Dataset 
std_df["Total_marks"] = std_df["Maths"]+std_df["Science"]+std_df["English"]
print("Dataset after adding Total Marks: \n",std_df)

#adding a new percentage column in the dataset
std_df["Percentage"] = (std_df["Total_marks"]/300)*100
print("Dataset after adding Percentage: \n",std_df)

#finding the top performer among all the students 
top_performer = std_df["Total_marks"].idxmax()
print("Top Performer of Among the all Students: \n", top_performer+1)

#finding average marks by class 
avg_Marks = std_df.groupby("Class")["Total_marks"].mean()
print("Average Marks By Class: \n",avg_Marks)

#Saving the Clean Dataset
std_df.to_csv("Student Data.csv", index=False)