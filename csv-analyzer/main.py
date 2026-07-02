#This project will describe a csv anlyser with panda
import pandas as pd
# using the csv file on dataFrame
df = pd.read_csv('sales.csv')

#Testing the import
print(f"Here are the frist five products in my shop: \n\n\n{df.head()}\n\n")
# print(df.info())
# print(df.describe())

print("There are the smalls stats in my shop: \n")

#Calculate the total revenue and the most sold product
df['total_amount'] = df['quantity'] * df ['price']
total_sold = df['total_amount'].sum() #Total revenue

print(f"Total sold :\t {total_sold} FCFA this mont \n\n")

best_seller = df['total_amount'].idxmax() #id of best seller
product_name = df.loc[best_seller, 'product'] #name of the best seller product
seller_sold = df.loc[best_seller, 'total_amount'] #total best seller solds

print(f"Best seller product:\t {product_name} with {seller_sold} FCFA sold this month")