import pandas as pd


df = pd.DataFrame({
    "Name" : ["Alice", "Bob", "Charlie"],
    "Age" : [25, 30, 35],
    "City" : ["New York", "Los Angeles", "Chicago"]
})   

# print(df)

df["Salary"] = [50000, None, 70000]
# print(df)
# print(df.info())

# delete none values
# df["Salary"] = df["Salary"].fillna(0)  # fillna() method is used to replace the missing values with a specified value. In this case, we are replacing the None values in the "Salary" column with 0.
# print(df)

# delete rows with none values
new_df = df.dropna()  # dropna() method is used to remove the rows that contain missing values. In this case, we are creating a new DataFrame called new_df that contains only the rows from df that do not have any None values.
print(new_df)



