import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('students.csv')

# Calculate the average marks across all columns except 'Name'
df['Average'] = df.loc[:, 'Math':'English'].mean(axis=1)

# Display the results
for index, row in df.iterrows():
    print(f"Student: {row['Name']}, Average Marks: {row['Average']:.2f}")
