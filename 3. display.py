# head() 5
# tail() 5

import pandas as pd

df = pd.read_json("sample_Data.json")

# Display the first 5 rows of the DataFrame
print(df.head(5))


# Display the last 5 rows of the DataFrame
print(df.tail(5))