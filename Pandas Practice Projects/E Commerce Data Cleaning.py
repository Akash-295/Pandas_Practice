
#E Commerce Data Cleaning Project (Intermediate)

# Tasks
# Detect missing values.
# Fill missing prices using median.
# Fill missing stock using mean.
# Remove duplicate products.
# Generate summary report.

import pandas as pd

e_commerce = pd.read_csv("E-Commerce.csv")
print(e_commerce)

print("Detecting Null Values in the Dataset: \n",e_commerce.isnull().sum())

price_median = e_commerce["Price"].median()
print(e_commerce["Price"].fillna(price_median))
 
stock_mean = e_commerce["Stock"].mean()
print(e_commerce["Stock"].fillna(stock_mean))

print(e_commerce["Product"].duplicated())
print(e_commerce["Product"].drop_duplicates())

print(e_commerce.describe())

e_commerce.to_csv("E-Commerce.csv")