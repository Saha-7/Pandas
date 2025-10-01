import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}


df = pd.DataFrame(data)
print(df)

# Save DataFrame to a CSV file
#df.to_csv('output.csv', index=False)


# Save DataFrame to an Excel file
#df.to_excel('output.xlsx', index=False)


# Save DataFrame to a JSON file
df.to_json('output.json', orient='records', lines=True)