import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Age": [25, 30, 35, 40, 28, 33, 38, 29, 31, 27],
    "Salary": [50000, 60000, 70000, 80000, 55000, 65000, 75000, 58000, 62000, 52000]
}


df = pd.DataFrame(data)
print(df)

print("\n")
# Selecting rows based on a condition
# Example: Select rows where Age is greater than 30
filtered_df = df[df["Age"] > 30]
print(filtered_df)



print("\n")
# Selecting rows on multiple conditions
# Example: Select rows where Age is greater than 30 and Salary is greater than 60000
filtered_df_multi = df[(df["Age"] > 30) & (df["Salary"] > 60000)]
print(filtered_df_multi)