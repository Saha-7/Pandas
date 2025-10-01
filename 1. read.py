import pandas as pd

# Load a CSV file into a DataFrame
# df = pd.read_csv('sales_data_sample.csv', encoding='latin1')


# Load an Excel file into a DataFrame
# df = pd.read_excel('SampleSuperstore.xlsx', engine="xlrd")


# Load a JSON file into a DataFrame
df = pd.read_json("sample_Data.json", )
print(df)