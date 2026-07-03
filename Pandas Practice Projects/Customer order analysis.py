
#Customer Order Analysis (Intermediet)

import pandas as pd

customers = pd.read_csv("customers.csv")
print("Customer: \n",customers)

orders = pd.read_csv("orders.csv")
print("Orders: \n", orders)

#merging the both datasets 
cust_orders = pd.merge(
    customers,orders
)
print(cust_orders)

#Total spending per customer
total_spen = cust_orders.groupby("Name")["Amount"].sum()
print("Total Spending per Customer: \n", total_spen)

#Highest Spending Customer 
high_spen = cust_orders.groupby("Name")["Amount"].max().idxmax()
print("highest spending Customer: \n", high_spen)

#Average order Amount
avg_order_amount = cust_orders["Amount"].mean()
print("Average Order Amount: \n", avg_order_amount)

#Order per city
order_per_city = cust_orders.groupby("City").size()
print(order_per_city)