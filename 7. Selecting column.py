import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Age": [25, 30, 35, 40, 28, 33, 38, 29, 31, 27],
    "Salary": [50000, 60000, 70000, 80000, 55000, 65000, 75000, 58000, 62000, 52000]
}


df = pd.DataFrame(data)
print(df)

# Select a single column returns a Series
print("Name column:")
print(df["Salary"])

# Select multiple columns returns a DataFrame
print("\nName and Salary columns:")
print(df[["Name", "Salary"]])