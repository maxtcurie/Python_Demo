import pandas as pd

# Create two example dataframes
df1 = pd.DataFrame({'A': [1, 2, 3],
                    'B': ['a', 'b', 'c']})

df2 = pd.DataFrame({'A': [4, 5, 6],
                    'B': ['d', 'e', 'f']})


# Concatenate along columns (axis=1)
concatenated_df = pd.concat([df1, df2], axis=1)

concatenated_df2 = pd.concat([df1, df2], axis=0, ignore_index=True)

print("Dataframe 1:")
print(df1)
print("\nDataframe 2:")
print(df2)
print("\nConcatenated Dataframe (axis=1):")
print(concatenated_df)

print("\nConcatenated Dataframe (axis=0):")
print(concatenated_df2)