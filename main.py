import tabula
import os
import pandas as pd

# Function to convert PDF to CSV
def convert_pdf_to_csv(pdf_file_path, csv_file_path):
    # Using tabula to extract table into a DataFrame
    # df = tabula.read_pdf(pdf_file_path, pages='all', stream=True)
    df = tabula.read_pdf(pdf_file_path, pages='all')[0]
    df = df.replace({'\r':' '}, regex=True)
    print(df)

    # Saving the DataFrame into a CSV file
    df.to_csv(csv_file_path, index=False)

# def convert_pdf_to_csv(pdf_file_path, csv_file_path, lattice=True, stream=False):
#     # Using tabula to extract tables into a list of DataFrames
#     df_list = tabula.read_pdf(pdf_file_path, pages='all', multiple_tables=True, 
#                               lattice=lattice, stream=stream, output_format="dataframe")

#     # Concatenating all tables into a single DataFrame
#     df = pd.concat(df_list, ignore_index=True)

#     # Replace '\r' in all cells with a white space
#     df = df.replace({'\r': ' '}, regex=True)

#     # Saving the DataFrame into a CSV file
#     df.to_csv(csv_file_path, index=False)

#     print(df)

# Example usage
pdf_file = 'input.pdf'  # Replace with your PDF file path
csv_file = 'output.csv'  # Desired output CSV file name

convert_pdf_to_csv(pdf_file, csv_file)
