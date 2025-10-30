#read in a csv file of homes data and create a dataframe
import pandas as pd

df_homes = pd.read_csv('homes_data.csv')

#print out the demnsion of the data frame adn the first ten rows

shape = df_homes.shape
print('DataFrame shape:', shape)
print(f' the homes data has shape of {shape[0]} rows and {shape[1]} columns')


# select only the homes with 500 or more units
df_big_homes = df_homes.drop(columns = ["id","easement"])
print(df_homes.head(10))



print(df_big_homes.head(10))

# look at the data types 
print(df_big_homes.dtypes)

#drop rows with missing values
df_big_homes_cleaned = df_big_homes.dropna()
#drop the duplicate rows
df_big_homes_cleaned = df_big_homes_cleaned.drop_duplicates()

#print out the first 10 rows of the cleaned dataframe
print('AFTER DROPPING NULLS AND DULICATES')
print(df_big_homes_cleaned.head(10))

# Convert sale_price to numeric, setting non-numeric values to NaN
df_big_homes['sale_price'] = pd.to_numeric(df_big_homes['sale_price'], errors='coerce')
# Filter for homes with sale_price > 0
df_big_homes = df_big_homes[df_big_homes["sale_price"] > 0]
print(df_big_homes.head(10))

#calculate average sale price
average_price = df_big_homes['sale_price'].mean()
print(f'The average sale price of big homes is: ${average_price:,.2f}')

