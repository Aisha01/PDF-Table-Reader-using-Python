import camelot
import csv
import os

# Directory containing your PDF files
directory_path = 'input'

# Path to your output CSV file
csv_file_path = 'output_4.csv'

# Function to process the first column (skipping every odd '\n')
def process_first_column(first_col):
    lines = first_col.split('\n')
    combined_lines = [' '.join(lines[i:i+2]) for i in range(0, len(lines), 2)]
    return combined_lines

# Function to handle multiline cells in all columns, excluding "CODICE" column
def split_multiline_rows(rows, codice_index):
    new_rows = []
    for row in rows:
        # Exclude the "CODICE" column
        row = row[:codice_index] + row[codice_index+1:]
        first_col_processed = process_first_column(row[0])
        remaining_cols = [col.split('\n') for col in row[1:]]
        max_splits = max(len(first_col_processed), *[len(col) for col in remaining_cols])
        while len(first_col_processed) < max_splits:
            first_col_processed.append('')
        for col in remaining_cols:
            while len(col) < max_splits:
                col.append('')
        for i in range(max_splits):
            new_row = [first_col_processed[i]] + [col[i] for col in remaining_cols]
            new_rows.append(new_row)
    return new_rows

# Write tables to CSV
with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory_path, filename)
            tables = camelot.read_pdf(file_path, pages='all', flavor='lattice')
            for table in tables:
                # Find the index of the "CODICE" column in the header
                if table.data:
                    header = table.data[0]
                    codice_index = header.index("CODICE") if "CODICE" in header else -1
                    # Process and write rows, excluding "CODICE" column
                    split_rows = split_multiline_rows(table.data[1:], codice_index) # Skip header row
                    for row in split_rows:
                        writer.writerow(row)

print("CSV file has been created with data from all PDF files, excluding 'CODICE' column.")
