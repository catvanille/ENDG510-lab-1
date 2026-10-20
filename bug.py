import pandas as pd # in case of error, install pnadas using: pip install pandas
import numpy as np
# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

i = 1000
while i>=0:
    new_data = {
    'Temp': np.random.randint(400),
    'Humd': np.random.randint(200),
    'Label': 0
    }
    df = df._append(new_data, ignore_index=True)
    i=i-1
# Step 3: Save the DataFrame to a new CSV file
df.to_csv("databug.csv", index=False)