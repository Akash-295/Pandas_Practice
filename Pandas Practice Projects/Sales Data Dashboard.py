
#Sales Data Dashboard (Intermediet)

import pandas as pd

sales_df = pd.read_csv("Sales_Dataset.csv")
print(sales_df)

revenue = sales_df["Quantity"]*sales_df["Price"]
sales_df["Revenue"] = revenue
print("After adding Revenue column: \n", sales_df)

#Total Revenue
total_rev = sales_df["Revenue"].sum()
print("Total Revenue: \n", total_rev)

#Revenue By Category
rev_by_category = sales_df.groupby("Category")["Revenue"].sum()
print("Revenue By Category: \n",rev_by_category)

#Best selling Product
best_product = sales_df.groupby("Product")["Quantity"].max().idxmax()
print("Best Selling Product: \n",best_product)

#Best Revenue Product
best_rev_product = sales_df.groupby("Product")["Revenue"].max().idxmax()
print("Best Revenue Product: \n", best_rev_product)

#Average order value
avg_order = sales_df["Quantity"].mean()
print("Average Order Value: \n", avg_order)