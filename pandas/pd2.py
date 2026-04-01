# iloc and loc

import pandas as pd

# iloc - nó sẽ dựa theo chỉ số của hàng và cột ( hàng và cột được đánh số từ 0)

# loc - dựa theo labels (index) của hàng vào cột ( tên cột và tên hàng)
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': ["G", "H", "K"]
})   

# print(df)   

# print(df.loc[[0, 2]])

# ket hop hang voi cot
# chon tat ca cac hang voi 1 cot
# print(df.loc[:, 'C']) # chon tat ca cac hang voi cot A
# print(df.loc[:, ['C', "A"]]) # chon tat ca cac hang voi cot A va C  


# chon 1 hang voi cot co dinh
# print(df.loc['X', 'C']) # chon hang X voi cot C


# iloc
# print(df.iloc[[0]]) # chon hang 0

# lay tat ca cac hang voi cac cot
# print(df.iloc[:, [0, 2]]) # chon tat ca cac hang voi cot A va C


# set index 

new_df = df.set_index('A') # set cot A lam index
# print(new_df)


print(new_df.loc[2]) # chon hang 1 voi cot C



