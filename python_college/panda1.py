import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
    'C': [4.5, 5.5, 6.5]
})
print(df)

# Accessing a value (row 1, column 'B')
value = df.loc[1, 'B']
print("Value at row 1, column 'B':", value)

# Selecting column 'C'
cols = df.loc[:, ['A', 'B']]
print(cols)

# # Filtering
# filtered_df = df[df['A'] > 1]
# print(filtered_df)

# # np.nan means not a number
# df.isna()  # Check for NaN values
# df.fillna(0)  # Fill NaN values with 0

# # applying transformation functions
# df['A'] = df['A'].apply(lambda x: x * x)
# print(df['A'])