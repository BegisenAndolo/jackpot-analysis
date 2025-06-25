#Import the directory pandas and csv
import pandas as pd
import csv

#open the csv file using its file path and assign it a variable file
with open('C:/Users/LENOVO/Documents/Pastor Beggy/Project/jackpot-analysis/staging_data.csv') as file:
    df = pd.read_csv(file, encoding='utf-8-sig')

#print the dataframe
print(df)

#trpe of data type for the df
type(df)

#understanding the structure of the data
print(df.columns)

#printing col names for data validation
for col in df.columns:
    print(f"'{col}'")

#stripping white space and Byte Order Mark form the col names
df.columns = [col.strip().replace('\ufeff', '') for col in df.columns]
print(df.columns.tolist()) 

#reading the first col to fix BOM
first_col = df.columns[0]
print(f"raw first column: {repr(first_col)}")
df.columns = [col.replace('ï»¿', '') for col in df.columns]
print(df.columns.tolist())

#used a .join to rewrite col headers
df.columns = [''.join(char for char in col if ord(char) < 128) for col in df.columns]
print(df.columns.tolist())
type(df.columns)
#inspecting the data in staging_data
print(df.head())

#cleaning the weight columns
weight_columns = df.columns[-5:]
print(weight_columns.tolist())
type(weight_columns)

#looping through weight cols to clean the values to floats
for col in weight_columns:
    df[col] = df[col].astype(str).str.replace('%', '').astype(float) / 100
df.head()

#calculating the correlation between correct picks and weights
columns_to_check = ['Correct_Picks'] + weight_columns.tolist()
correlations = df[columns_to_check].corr()
#print just the row for correlation
print("\ncorrelation with correct_picks:\n")
print(correlations['Correct_Picks'])