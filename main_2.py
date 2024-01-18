import camelot
import pandas as pd

# Function to convert PDF to CSV using Camelot
def convert_pdf_to_csv_camelot(pdf_file_path, csv_file_path):
    # Using Camelot to extract tables from PDF
    tables = camelot.read_pdf(pdf_file_path, pages='all', flavor='lattice')

    # Check if any tables were found
    if tables.n == 0:
        print("No tables found in PDF.")
        return

    # Concatenate all tables into a single DataFrame
    all_tables = pd.concat([t.df for t in tables], ignore_index=True)

    # Process each cell to split by '\n' and expand the DataFrame
    expanded_rows = []
    for index, row in all_tables.iterrows():
        # print(row[0])
        # Split each cell in the row by '\n'
        split_cells = [cell.split('\n') for cell in row]

        print(split_cells[0])

        # Find the maximum number of lines any cell in this row has been split into
        max_lines = max(len(cell) for cell in split_cells)
        print(max_lines)

        # Ensure each cell has the same number of lines, filling with empty strings if necessary
        for cell in split_cells:
            cell.extend(['n/a'] * (max_lines - len(cell)))

        # Transpose the split cells to create new rows
        for i in range(max_lines):
            new_row = [cell[i] for cell in split_cells]
            expanded_rows.append(new_row)
        
        print(expanded_rows)

    # Creating a new DataFrame from the expanded rows
    expanded_df = pd.DataFrame(expanded_rows, columns=all_tables.columns)

    # Saving the expanded DataFrame into a CSV file
    expanded_df.to_csv(csv_file_path, index=False)

# Example usage
pdf_file = 'input.pdf'  # Replace with your PDF file path
csv_file = 'output.csv'  # Desired output CSV file name

convert_pdf_to_csv_camelot(pdf_file, csv_file)