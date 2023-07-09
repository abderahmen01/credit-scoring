import pandas as pd

def delete_column_from_csv(input_file, output_file, column_name):
    df = pd.read_csv(input_file)  # Read the input CSV file into a DataFrame
    df = df.drop(column_name, axis=1)  # Drop the specified column

    df.to_csv(output_file, index=False)  # Write the updated DataFrame to the output CSV file

    print(f"Column '{column_name}' deleted from the CSV file '{output_file}'.")

# Example usage
input_file = 'data3.csv'
output_file = 'data3.csv'
column_name = 'class'

delete_column_from_csv(input_file, output_file, column_name)
