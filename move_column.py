import pandas as pd

# Specify the input and output file paths
input_file = 'data3.csv'
output_file = 'data3.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(input_file)

# Specify the column to be moved to the last position
column_to_move = 'class'

# Get the list of columns excluding the column to be moved
columns = [col for col in df.columns if col != column_to_move]

# Reorder the columns and move the desired column to the last position
new_columns = columns + [column_to_move]
df = df[new_columns]

# Save the DataFrame to a new CSV file
df.to_csv(output_file, index=False)
