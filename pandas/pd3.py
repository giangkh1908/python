import pandas as pd


df = pd.DataFrame({
    "Name" : ["Alice", "Bob", "Charlie"],
    "Age" : [25, 30, 35],
    "City" : ["New York", "Los Angeles", "Chicago"]
})   


# get data by column name
# print(df["Name"]) # get column Name


# filter row based on a condition - Loc cac hang du lieu
# filtered = df[df["Age"] > 30]
# print(filtered)

# change data in dataframe
# add new column
# df["col"] = ["a", "b", "c"]
# # print(df)

# # delete column
# new_df = df.drop("City", axis=1) # axis=1 means drop column, axis=0 means drop row
# print(new_df)

# change value in  ô  nào đấy
print(df)
df.loc[0, "Name"] = "Alice Smith"
print(df)






