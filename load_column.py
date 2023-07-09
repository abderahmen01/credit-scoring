import pandas as pd
def extract_column_values(input_file1, column_name1):
    df = pd.read_csv(input_file1)  # Read the input CSV file into a DataFrame
    column_values = df[column_name1].tolist()  # Extract column values and store them in a list

    return column_values

# Example usage
input_file1 = 'C:\\Users\\benaz\\Desktop\\German_processed.csv'
column_name1 = 'class'

values_list = extract_column_values(input_file1, column_name1)
def add_column_to_csv(input_file, output_file, column_name, column_data):
    df = pd.read_csv(input_file)  # Read the input CSV file into a DataFrame
    df[column_name] = column_data  # Add the new column to the DataFrame

    df.to_csv(output_file, index=False)  # Write the updated DataFrame to the output CSV file

    print(f"Column '{column_name}' added to the CSV file '{output_file}'.")

# Example usage
input_file = 'data3.csv'
output_file = 'data3.csv'
column_name = 'target'
column_data = values_list  # Assuming 3 rows of data

add_column_to_csv(input_file, output_file, column_name, column_data)
