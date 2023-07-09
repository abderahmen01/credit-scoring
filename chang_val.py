import pandas as pd

def change_multiple_csv_values(input_file, output_file, column_name, old_values, new_value):
    df = pd.read_csv(input_file)  # Read the input CSV file into a DataFrame
    df[column_name] = df[column_name].replace(old_values, new_value)  # Change multiple values in the specified column

    df.to_csv(output_file, index=False)  # Write the updated DataFrame to the output CSV file

    print(f"Values in column '{column_name}' changed to '{new_value}' in the CSV file '{output_file}'.")

# Example usage

input_file = 'data3.csv'
output_file = 'data3.csv'
column_name = 'target'
old_values = 3  # List of old values to be replaced
new_value = 0

change_multiple_csv_values(input_file, output_file, column_name, old_values, new_value)
