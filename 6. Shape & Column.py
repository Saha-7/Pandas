
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Age": [25, 30, 35, 40, 28, 33, 38, 29, 31, 27],
    "Salary": [50000, 60000, 70000, 80000, 55000, 65000, 75000, 58000, 62000, 52000]
}


df = pd.DataFrame(data)
print(df)


# Get the shape of the DataFrame
print(f"Shape of the DataFrame: {df.shape}")

# Get the columns of the DataFrame
print(f"Columns in the DataFrame: {df.columns}")