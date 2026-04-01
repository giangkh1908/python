import pandas as pd

# load data from csv file
data = pd.read_csv('data.csv')

# print(type(data))
# print(data)
# print(data.head(1)) # default is 5 rows, you can specify the number of rows to display by passing an argument to head() method, for example: data.head(10) will display the first 10 rows of the data.
# print(data.tail()) # default is 5 rows, you can specify the number of rows to display by passing an argument to tail() method, for example: data.tail(10) will display the last 10 rows of the data.

# save file .csv
# data.to_csv('data_copy.csv', index=False) # index=False will prevent pandas from writing row indices to the file. If you want to include row indices in the output file, you can set index=True or simply omit the index parameter, as it defaults to True.

# inspect data
# print(data.info()) # provides a concise summary of the DataFrame, including the number of non-null entries, data types of each column, and memory usage. This is useful for understanding the structure of the data and identifying any potential issues such as missing values or incorrect data types.

# print(data.describe()) # generates descriptive statistics of the DataFrame, including count, mean, standard deviation, minimum, 25th percentile, median (50th percentile), 75th percentile, and maximum values for each numeric column. This is useful for understanding the distribution and central tendency of the data.

print(data.columns)
print(data.index)


