
import pandas as pd

emp_df = pd.read_csv("Employee Data.csv")
print(emp_df)

#average Salary By department
avg_sal = emp_df.groupby("Department")["Salary"].mean()
print("Average Salary By Department: \n", avg_sal)

#Highest and Lowest Salary
Sal_config = emp_df["Salary"].agg(['max','min'])

print("Highest and Lowest Salary: \n", Sal_config)


#Department with Highest average salary

high_sal_dept = emp_df.groupby("Department")["Salary"].mean().idxmax()
print("Highest Average Salary of Department: \n", high_sal_dept)

#Employee earning above average salary
emp_earn = emp_df[emp_df["Salary"]>emp_df["Salary"].mean()]
print("Employees earning above average Salary: \n",emp_earn)